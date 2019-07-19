"""
A short code I made whilst playing around with the sys and pkgutil modules. 
It displays a list of Python builtins first, followed by a list of all of the modules installed.
"""

import sys, pkgutil

print("Python builtins: \n" + ("="*15) + "\n" + str(sys.builtin_module_names))

print("\n" + ("="*40) + "\n")

mods = list(mod[1] for mod in pkgutil.iter_modules())

print("Sololearn Installed Modules: \n" + ("="*27) + "\n" + str(mods))
