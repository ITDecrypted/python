# Same functionalities as ls_cli.py
# But now argparse.ArgumentParser() creates a new ArgumentParser object
# This object will handle details such as how many arguments are allowed.

# Powerful argument handler
from argparse import ArgumentParser

# For objects that represent paths to files or directories
from pathlib import Path

parser = ArgumentParser()

# Positional argument
# Reference: https://docs.python.org/3/library/
# argparse.html#argparse.ArgumentParser.add_argument
parser.add_argument('path')

# Argument handling
# Ref: https://docs.python.org/3/library/argparse.html#invalid-arguments
args = parser.parse_args()

# args.path is a dynamic attribute (an attribute created at runtime for
# that instance). It belongs to the simple Namespace object args
# (designed for holding attributes only)
dir_ = Path(args.path)

# The rest is the same as ls_cli.py
if not dir_.is_dir():
	parser.error(f'{dir_} is not a directory')

for entry in dir_.iterdir():
	print(entry.name)
