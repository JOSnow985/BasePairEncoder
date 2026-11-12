# convert amino acids to codons 
def aminos_to_codons(aminos):
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
    reversed_code = {value: key for key, value in genetic_code.items()}
    return [reversed_code[amino] for amino in aminos]

# flip RNA bases to DNA bases
def rna_to_dna(codons):
    pairs = {'C': 'G', 'U': 'A', 'A': 'T', 'G': 'C'}
    return ["".join(pairs[base] for base in codon) for codon in codons]

def combine_sequence(sequence):
    return ' '.join(sequence)

if __name__ == "__main__":
    input = input("Enter sequence:\nMSG = ")
    aminos = list(input)
    codons_rna = aminos_to_codons(aminos)

    rna_seq = " ".join(codons_rna)
    print("RNA = " + rna_seq)

    codons_dna = rna_to_dna(codons_rna)
    dna = combine_sequence(codons_dna)
    print("DNA = " + dna)