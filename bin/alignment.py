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
from Bio import AlignIO


# CLASSES
class alignment:
    """ Desc """

    def __init__(self, file_path):
        self.file_list = file_path
        self.align = AlignIO.read(file_path, "fasta")

    def __str__(self):
        return self.align.__str__()
