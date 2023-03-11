<p align="center">
<a href="https://github.com/denisidoro/navi">navi</a> (interactive cli cheatsheet) integration into <a href="https://xon.sh/">xonsh</a> (shell)
</p>

<p align="center">  
If you like the idea click ⭐ on the repo
</p>


## Installation

To install use pip:

```xsh
xpip install xontrib-navi
# or: xpip install -U git+https://github.com/eugenesvk/xontrib-navi
```

## Usage

1. Add the following to your `.py` xontrib loading config and `import` it in your xonsh run control file (`~/.xonshrc` or `~/.config/rc.xsh`):
```py
from xonsh.xontribs 	import xontribs_load
from xonsh.built_ins	import XSH
envx = XSH.env

xontribs = [ "navi", # Initializes navi (interactive cli cheatsheet)
 # your other xontribs
]
# ↓ optional configuration variables (use `False` to disable a keybind)
if 'navi' in xontribs: # Configure navi only if you're actually loading it
  # config var      	  value	 |default|alt_cmd¦ comment
  envx["X_NAVI_KEY"]	= "⎈g" 	#|c-g|   False¦ Autofill existing command with navi's best match or launch navi if no good match found

xontribs_load(xontribs) # actually load all xontribs in the list
```

2. Or just add this to your xonsh run control file
```xsh
xontrib load navi # Initializes navi (interactive cli cheatsheet)
# configure like in the example above, but replace envx['VAR'] with $VAR
$X_NAVI_KEY	= "c-g" # ...
```


## Known issues

- Bottom toolbar may temporary disappear on some invokations of the commands in this xonrib likely due to this [xonsh issue](https://github.com/xonsh/xonsh/issues/5084)
- The match currently works only for the whole prompt, so `git sta` will get autofilled to its best navi match of `git status`, but `git show; git sta` will fail to find any match and do nothing

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template)
