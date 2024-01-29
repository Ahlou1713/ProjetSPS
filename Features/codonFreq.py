# Calculer les fréquences de codons dans la chaîne ADN
from Features.DNATranscript import dna_to_rna
from Features.DNATranslation import rna_to_prot

# from Features.DNATranslation import codon_tab


def freq_codon(dna):
    d = {}
    rna = dna_to_rna(dna)
    for i in range(0, len(rna), 3):
        codon = rna[i : i + 3]
        if codon in d:
            d[codon] += 1
        else:
            d[codon] = 1

    return d
