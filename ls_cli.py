# Building the ls command from scratch
# In order to understand the underlying functionality of it

# For sys.argv which is a list containing the number of arguments
# passed to the command
# (https://docs.python.org/3/library/sys.html#sys.argv)
import sys

# For creating Path objects designed to represent paths to a file
# (or filesystem)
from pathlib import Path

# There are always two arguments for sys.argv with regards to ls
# 1) The command itself (in this case, ls)
# 2) The file name or file system for listing its contents
# Therefore, only accept two arguments for ls.

# Assignment expression, AKA the "walrus operator"
if (num_args := len(sys.argv)) > 2:
    sys.exit(f'expected one argument; got {num_args - 1}')
elif num_args < 2:
	sys.exit(f'target directory missing')

dir_ = Path(sys.argv[1])

# https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir
# determines if a path is a directory or not
if not dir_.is_dir():
	sys.exit(f'{dir_} is not a directory')

# Now that the input has satisfied the "security check",
# we can list the contents of it because we have checked
# that it is indeed a directory.

# Returns Path objects of the contents of the directory
for entry in dir_.iterdir():

	# Prints the final part of the path
	# This works as Path is a child of PurePath
	# Thus inheriting its methods and attributes
	print(entry.name)
