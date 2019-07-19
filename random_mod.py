"""
A short code created to list all of the modules installed. 
It returns the documentation for a random module.
"""

import pkgutil
from random import choice

mods = list(mod[1] for mod in pkgutil.iter_modules())

print(help(choice(mods)))
