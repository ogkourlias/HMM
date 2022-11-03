#!/usr/bin/env python3

"""
    usage:
        python3 main.py
"""

# METADATA VARIABLES
__author__ = "Orfeas Gkourlias"
__status__ = "WIP"
__version__ = "0.1"

# IMPORT
import subprocess

# CLASSES
class hmmer:
    """ Desc """
    def __init__(self, msa):
        self.msa = msa

    def hmmer_scan(self):
        subprocess.run(['hmmbuild', '../data/hmm_out.hmm', self.msa])
        subprocess.run(['hmmpress', '-f', '../data/hmm_out.hmm'])
        subprocess.run(['hmmscan', '--tblout', '../data/scan.txt','../data/hmm_out.hmm', '../data/pou_fam.fasta'])
        subprocess.run(['hmmsearch', '--tblout', '../data/search.txt','../data/hmm_out.hmm', '../data/pou_fam.fasta'])
