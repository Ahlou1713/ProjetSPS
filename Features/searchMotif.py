# Chercher un motif dans la chaîne ADN
def search_motif(dna, motif):
    positions = []

    for i in range(len(dna) - len(motif) + 1):
        if dna[i : i + len(motif)] == motif:
            positions.append(i + 1)

    return positions