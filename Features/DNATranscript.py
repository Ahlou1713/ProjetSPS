
# Transcrire la chaîne ADN en une chaîne ARN
def dna_to_rna(dna):
    rna = ""
    for n in dna:
        if n == "A":
            rna += "U"
        elif n == "T":
            rna += "A"
        elif n == "C":
            rna += "G"
        elif n == "G":
            rna += "C"

    return rna