# Réaliser des mutations aléatoires sur la chaîne ADN
import random


def dna_mutation(dna, num):
    mut_dna = dna
    mut_index = random.sample(range(0, len(dna)), num)

    print(f"Mutation indexes : {mut_index}")
    for m in mut_index:
        mut_dna = mut_dna[:m] + random.choice(["A", "T", "C", "G"]) + mut_dna[m + 1 :]

    return mut_dna