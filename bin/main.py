#!/usr/bin/env python3

"""
    usage:
        python3 main.py
"""

# METADATA VARIABLES
__author__ = "Orfeas Gkourlias"
__status__ = "WIP"
__version__ = "0.1"

# IMPORTS
import sys
from alignment import alignment
import hmmer

# CLASSES
class x():
    """ Desc """


# FUNCTIONS
def y():
    """ Desc """
    return 0


# MAIN
def main(args):
    """ Main function """
    aln = alignment(sys.argv[1])
    print(aln)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
