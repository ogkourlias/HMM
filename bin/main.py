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
from hmmer import hmmer


# MAIN
def main(args):
    """ Main function """
    hmmer_inst = hmmer(sys.argv[1])
    hmmer_inst.hmmer_scan()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
