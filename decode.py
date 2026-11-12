# split a string into 3s
def sequence_to_codons(sequence):
    return [sequence[i:i+3] for i in range(0, len(sequence), 3)]

def sequence_to_codons_spaces(sequence:str):
    return sequence.split(" ")

# flip DNA bases to RNA bases
def dna_to_rna(codons):
    pairs = {'G': 'C', 'A': 'U', 'T': 'A', 'C': 'G'}
    return ["".join(pairs[base] for base in codon) for codon in codons]

# flips bases in rna
def flip_rna(codons):
    pairs = {'C': 'G', 'U': 'A', 'A': 'U', 'G': 'C'}
    return ["".join(pairs[base] for base in codon) for codon in codons]

# flips bases in dna
def flip_dna(codons):
    pairs = {'C': 'G', 'T': 'A', 'A': 'T', 'G': 'C'}
    return ["".join(pairs[base] for base in codon) for codon in codons]

# convert mRNA codons to amino acids
def codons_to_aminos(codons):
    genetic_code = {
        'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
        'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',
        'UUA': 'L', 'UCA': 'S', 'UAA': ' ', 'UGA': ' ',
        'UUG': 'L', 'UCG': 'S', 'UAG': ' ', 'UGG': 'W',
        'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',
        'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
        'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
        'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
        'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',
        'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
        'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
        'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
        'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',
        'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
        'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
        'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'

    }
    return [genetic_code[codon] for codon in codons]

def combine_sequence(sequence):
    return ''.join(sequence)

if __name__ == "__main__":
    input = input("Enter sequence:\nDNA = ")
    codons = sequence_to_codons_spaces(input)

    codons_rna = dna_to_rna(codons)
    rna_seq = " ".join(codons_rna)
    print("RNA = " + rna_seq)

    aminos = codons_to_aminos(codons_rna)
    message = combine_sequence(aminos)
    print("MSG = " + message)