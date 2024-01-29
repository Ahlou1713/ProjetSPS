
# Calculer le complément inverse de la chaîne ADN
def complement_dna(dna):
    dna_complement = ""
    for n in dna:
        if n == "A":
            dna_complement += "T"
        elif n == "T":
            dna_complement += "A"
        elif n == "C":
            dna_complement += "G"
        elif n == "G":
            dna_complement += "C"

    return dna_complement