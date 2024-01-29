import random

#Generer une chaîne ADN de taille n
def generate_random_dna(n):
    dna = ""
    for i in range(n):
        dna += random.choice(["A", "T", "C", "G"])
    return dna