
# Calculer les fréquences des bases nucléiques dans la chaîne ADN
def base_frequency(dna):
    d = {}
    for b in dna:
        if b in d:
            d[b] += 1
        else:
            d[b] = 1

    return d