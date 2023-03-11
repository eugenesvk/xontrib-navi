"""
navi (interactive cli cheatsheet) integration
"""
import re
import sys
import typing
import subprocess
from subprocess                      	import PIPE
from os                              	import environ, chdir  #
from pathlib                         	import Path     #
from xonsh.built_ins                 	import XSH
from prompt_toolkit.keys             	import ALL_KEYS
from xonsh.completers.path           	import complete_dir, _quote_paths
from xonsh.parsers.completion_context	import CompletionContextParser

__all__ = ()

envx      = XSH.env or {}
env       = environ
historyx  = XSH.aliases["history"]
eventx    = XSH.builtins.events
cdx       = XSH.aliases["cd"]

base='navi'

is_cmd_cache_fresh = False
def get_bin(base_in): # (lazily 1st) get the full path to navi binary from xonsh binary cache
  if type(base_in) == dict:
    if 'tmux' in base_in and envx.get("TMUX", ""):
      base = base_in['tmux']
    else:
      base = base_in['']
  else:
    base = base_in

  global is_cmd_cache_fresh
  bin   = XSH.commands_cache.lazy_locate_binary(base, ignore_alias=True)
  if not bin and not is_cmd_cache_fresh:
    is_cmd_cache_fresh = True
    bin = XSH.commands_cache.     locate_binary(base, ignore_alias=True)
  if not bin:
    PATH = envx.get("PATH")
    print(f"Cannot find '{base}' in {PATH}")
    return None
  else:
    return bin

def navi_proc_run(args): # Run a navi process with passed args and return it
  if not (bin_ := get_bin(base)):
    return

  full_cmd	= [bin_] + args
  proc    	= subprocess.run(full_cmd, stdout=PIPE)

  out   	= proc.stdout.decode().rstrip('\n')
  if err	:= proc.stderr:
    err 	= err.decode().rstrip('\n')
  retn  	= proc.returncode

  return (out, err, retn)

def navi_get_cheat_cmd(event): # Get best match or launch selector
  buf       	= event.current_buffer
  doc       	= buf.document
  pre_cursor	= doc.current_line_before_cursor
  text      	= doc.text

  current_cmd	= doc.text.strip()
  if not current_cmd: # no command, launch navi...
    args = ['--print'] #... to print to stdout
    choice,err,retn = navi_proc_run(args)
    event.cli.renderer.erase() # clear old output
    if   err:
      print(err, file=sys.stderr)
    elif choice:
      buf.text           	=     choice
      buf.cursor_position	= len(choice)
  else: # try to match current cmd
    args = ['--print','--best-match', '--query',current_cmd]
    best_match,err,retn = navi_proc_run(args)
    if   err:
      print(err, file=sys.stderr)
    elif not best_match: # can't match → do nothing
      pass
    elif     best_match and\
             best_match != current_cmd: # match≠command → use it
      # todo: fix to replace only current process, not the whole .text
      buf.text           	=     best_match
      buf.cursor_position	= len(best_match)
    else: # match=command → run an interactive process with our command as a query
      args = ['--print', '--query',current_cmd]
      out,err,retn = navi_proc_run(args)
      event.cli.renderer.erase() # clear old output
      if out: # todo: fix to replace only current process, not the whole .text
        buf.text           	=     out
        buf.cursor_position	= len(out)

  return

def _parse_key_user(key_user):
  _key_symb = {
    '⎈':'c-'  ,'⌃':'c-'   ,
    '▼':'down' ,'↓':'down' ,
    '▲':'up'   ,'↑':'up'   ,
    '◀':'left' ,'←':'left' ,
    '▶':'right','→':'right',
  }
  _alts = ['a-','⌥','⎇']

  for k,v in _key_symb.items(): # replace symbols
    if k in key_user: # replace other keys
      key_user = key_user.replace(k,v)
  for alt in _alts:
    if alt in key_user: # replace alt with an ⎋ sequence of keys
      key_user = ['escape', key_user.replace(alt,'')]
      break

  return key_user

re_despace = re.compile(r'\s', re.IGNORECASE)
def navi_keybinds(bindings, **_): # Add navi keybinds (when use as an argument in eventx.on_ptk_create)
  from prompt_toolkit.key_binding.key_bindings import _parse_key

  _default_keys = {
    "X_NAVI_KEY"	: "c-g",
    }

  def handler(key_user_var):
    def skip(func):
      pass

    key_user = envx.get(     key_user_var, None)
    key_def  = _default_keys[key_user_var]
    if   key_user == None:     # doesn't exist       → use default
      if type(key_def) == list:
        return bindings.add(*key_def)
      else:
        return bindings.add( key_def)
    elif key_user == False:    # exists and disabled → don't bind
      return skip
    else:                      # remove whitespace
      key_user = re_despace.sub('',key_user)

    key_user = _parse_key_user(key_user)

    if   type(key_user) == str  and\
         key_user in ALL_KEYS: # exists and   valid  → use it
      return bindings.add(key_user)
    elif type(key_user) == list and\
      all(k in ALL_KEYS or _parse_key(k) for k in key_user):
      return bindings.add(*key_user)
    else:                      # exists and invalid  → use default
      print_color("{BLUE}xontrib-navi:{RESET} your "+key_user_var+" '{BLUE}"+str(key_user)+"{RESET}' is {RED}invalid{RESET}; "+\
        "using the default '{BLUE}"+str(key_def)+"{RESET}'; run ↓ to see the allowed list\nfrom prompt_toolkit.keys import ALL_KEYS; print(ALL_KEYS)")
      if type(key_def) == list:
        return bindings.add(*key_def)
      else:
        return bindings.add( key_def)

  @handler("X_NAVI_KEY")
  def navi_cheat_cmd(event): # Match current command to the best cheat sheet or launch the selector
    navi_get_cheat_cmd(event)


def _activate_navi():
  if (bin := get_bin(base)):            # if navi exists register events↓
    eventx.on_ptk_create(navi_keybinds) # add custom navi keybinds

_activate_navi()
