<h1>Hidden Markov Model Finder.</h1>
This program allows for the POU5F1.aln MSA file to be used in the creation of
a HMM. This was done with the HMMER package from ebi.ac.uk. The main script
drives the automation of HMMER shell functions on POU5F1.aln. Because of the
database requirement (pou_fam in this case), it is not yet dynamic. You may
use your own database file and .aln file.

<h3>Requirements and Usage</h3>
Requirements: 
1. Python3 with the ability to import the subprocess package.
2. Unix shell.
3. HMMER must be installed and able to interact with the shell.

Usage:
1. Change directory to bin.
2. Insert into terminal: python3 main.py ../data/POU5F1.aln
