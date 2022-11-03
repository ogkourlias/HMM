#!/usr/bin/env python3

"""
    usage:
        python3 main.py ../data/POU5F1.aln
        Make sure to be in the BIN directory.
"""

# METADATA VARIABLES
__author__ = "Orfeas Gkourlias"
__status__ = "Final"
__version__ = "1.0"

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
