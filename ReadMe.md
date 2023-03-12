<p align="center">
<a href="https://github.com/denisidoro/navi">navi</a> (interactive cli cheatsheet) integration into <a href="https://xon.sh/">xonsh</a> (shell)
</p>

<p align="center">  
If you like the idea click ⭐ on the repo
</p>


## Install

```xsh
xpip install xontrib-navi
# or: xpip install -U git+https://github.com/eugenesvk/xontrib-navi
```

## Configure

- Add the following to your `.py` xontrib loading config and `import` it in your xonsh run control file (`~/.xonshrc` or `~/.config/rc.xsh`):
```py
from xonsh.xontribs 	import xontribs_load
from xonsh.built_ins	import XSH
envx = XSH.env

xontribs = [ "navi", # Initializes navi (interactive cli cheatsheet)
 # your other xontribs
] # ↓ optional configuration variables (use `False` to disable a keybind)
if 'navi' in xontribs: # Configure navi only if you're actually loading it
  # config var      	  value	 |default|alt_cmd¦ comment
  envx["X_NAVI_KEY"]	= "⎈g" 	#|c-g|   False¦ Autofill existing command with navi's best match or launch navi if no good match found
  # run to see the allowed list for ↑: from prompt_toolkit.keys import ALL_KEYS; print(ALL_KEYS)
  # Alt is also supported as either of: a- ⎇ ⌥ (converted to a prefix 'escape')
  # Control symbols are also supported as either of: ⎈ ⌃

xontribs_load(xontribs) # actually load all xontribs in the list
```

- Or just add this to your xonsh run control file
```xsh
xontrib load navi # Initializes navi (interactive cli cheatsheet)
# configure like in the example above, but replace envx['VAR'] with $VAR
$X_NAVI_KEY	= "c-g" # ...
```

## Use

- <kbd>⎈</kbd><kbd>g</kbd> run navi
- `git sta` <kbd>⎈</kbd><kbd>g</kbd> `git status` autoreplace with navi's best match
- `git status` <kbd>⎈</kbd><kbd>g</kbd> run navi with current command as search input
- `git sta‸; git show` <kbd>⎈</kbd><kbd>g</kbd> `git status‸; git show` autoreplace only the command at ‸cursor


## Known issues

- Bottom toolbar may temporary disappear on some invokations of the commands in this xonrib likely due to this [xonsh issue](https://github.com/xonsh/xonsh/issues/5084)

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template)
