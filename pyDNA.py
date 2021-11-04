###############################
##      Made by calamixy     ##
## Ported to Python from Lua ##
##    Started Nov 2 2021     ##
##   Finished Nov 3 2021     ##
##      210 lines of 🐍      ##
###############################

from colorama import Fore, Style

codonDictionary = {
  'U': {

    'U': {
        'U': "PHE",
        'C': "PHE",
        'A': "LEU",
        'G': "LEU"
    },
    'C': {
        'U': "SER",
        'C': "SER",
        'A': "SER",
        'G': "SER"
    },
    'A': {
        'U': "TYR",
        'C': "TYR",
        'A': "STOP",
        'G': "STOP"
    },
    'G': {
        'U': "CYS",
        'C': "CYS",
        'A': "STOP",
        'G': "TRP"
    }

  },

  'C': {
    'U': {
        'U': "LEU",
        'C': "LEU",
        'A': "LEU",
        'G': "LEU"
    },
    'C': {
        'U': "PRO",
        'C': "PRO",
        'A': "PRO",
        'G': "PRO"
    },
    'A': {
        'U': "HIS",
        'C': "HIS",
        'A': "GLN",
        'G': "GLN"
    },
    'G': {
        'U': "ARG",
        'C': "ARG",
        'A': "ARG",
        'G': "ARG"
    }
  },

  'A': {
    'U': {
        'U': "ILE",
        'C': "ILE",
        'A': "ILE",
        'G': "MET"
    },
    'C': {
        'U': "THR",
        'C': "THR",
        'A': "THR",
        'G': "THR"
    },
    'A': {
        'U': "ASN",
        'C': "ASN",
        'A': "LYS",
        'G': "LYS"
    },
    'G': {
        'U': "SER",
        'C': "SER",
        'A': "ARG",
        'G': "ARG"
    }
  },

  'G': {
    'U': {
        'U': "VAL",
        'C': "VAL",
        'A': "VAL",
        'G': "VAL"
    },
    'C': {
        'U': "ALA",
        'C': "ALA",
        'A': "ALA",
        'G': "ALA"
    },
    'A': {
        'U': "ASP",
        'C': "ASP",
        'A': "GLU",
        'G': "GLU"
    },
    'G': {
        'U': "GLY",
        'C': "GLY",
        'A': "GLY",
        'G': "GLY"
    }
  }

}

def convDNAtoRNA(sequence):
  iterations = 0
  unformattedDNA = sequence.replace(" ", "")
  charDNA_A = list(unformattedDNA.lower())
  codonDNA_A = []
  codonRNA_S = ""

# Turn DNA into codons

  for x in charDNA_A:
    iterations += 1
    if iterations < 3:
      codonDNA_A.append(x)

    if iterations == 3:
      iterations = 0
      codonDNA_A.append(x)
      codonDNA_A.append(' ')

# RNA into codons

  for x in codonDNA_A:
    if x == 'a':
      codonRNA_S = codonRNA_S + 'U'
    if x == 't':
      codonRNA_S = codonRNA_S + 'A'
    if x == 'c':
      codonRNA_S = codonRNA_S + 'G'
    if x == 'g':
      codonRNA_S = codonRNA_S + 'C'
    if x == ' ':
      codonRNA_S = codonRNA_S + ' '
  return codonRNA_S.strip()

def RNAtoPROTEIN(sequence):
  u_Sequence = sequence.upper()
  RNA_A = u_Sequence.split(' ')
  codon_D = {}
  protein_A = []
  protein_S = ""

# Get the individual bases of each codon

  for x in RNA_A:
    codon = list(x)
    codon_D[len(codon_D)+1] = codon

# Find proteins via bases

  for x in codon_D.values():
    
    b1 = x[0]
    b2 = x[1]
    b3 = x[2]

    protein_A.append(codonDictionary[b1][b2][b3])
    protein_A.append(' ')
  
  # Convert the protein list to a string

  for x in protein_A:
    protein_S = protein_S + x
    # Remove unnecessary spaces
  return(protein_S.strip())

# Define a dictionary for cache purposes

Seq_D = {}

mode = input(f"{Fore.YELLOW}Pick your mode:\n {Style.RESET_ALL} {Fore.RED}1: {Style.RESET_ALL} DNA -> RNA\n {Style.RESET_ALL} {Fore.RED}2: {Style.RESET_ALL} DNA-> Protein\n {Style.RESET_ALL} {Fore.RED}3: {Style.RESET_ALL} RNA-> Protein\n")

sequence = input(f"{Fore.YELLOW}Your mode is: " + mode + f". Please enter a sequence. (Make sure the length of it is divisible by 3.)\n{Style.RESET_ALL}")
Seq_D["s"] = str(sequence)
Seq_D["m"] = int(mode)

if Seq_D["m"] == 1:

  print(f"{Fore.YELLOW} RNA -> DNA: {Style.RESET_ALL}" + convDNAtoRNA(Seq_D["s"]))
if Seq_D["m"] == 2:

  print(f"{Fore.YELLOW} DNA -> Protein: {Style.RESET_ALL}" + RNAtoPROTEIN(convDNAtoRNA(Seq_D["s"])))

if Seq_D["m"] == 3:
  print(f"{Fore.YELLOW} RNA -> Protein: {Style.RESET_ALL}" + RNAtoPROTEIN(Seq_D["s"]))

##################################################################################################                          .*END OF FILE*.                     ############
######################################################################################
