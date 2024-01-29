
# Calculer le taux de GC de la séquence ADN
def gc_in_dna(dna):
    num_gc = 0
    for n in dna:
        if n in ["C", "G"]:
            num_gc += 1

    return (num_gc / len(dna)) * 100
