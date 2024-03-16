from libs import mylib

print("mymodule.py:", __name__)

# -- can't do relative imports from top-level file --

# from .libs import mylib  # -  will NOT work and produces an ERROR, because this file is at the TOP level (same with the code.py file, which runs __main__)

# -- parent imports --

import libs.operations.operator

from libs.operations import operator