import random


# Générer une chaîne ADN aléatoire
def creat_random_dna(n):
    dna = ""
    for i in range(n):
        dna += random.choice(["A", "T", "C", "G"])
    return dna


# Vérifier la validité de la chaîne ADN
def is_dna_valid(dna):
    return set(dna) <= set("ATCG")


# Calculer les fréquences des bases nucléiques dans la chaîne ADN
def base_freq(dna):
    d = {}
    for b in dna:
        if b in d:
            d[b] += 1
        else:
            d[b] = 1

    return d


# Transcrire la chaîne ADN en une chaîne ARN
def dna_to_rna(dna):
    return dna.replace("T", "U")


# Transcrire la chaîne ARN résultante en protéines (i.e., acides aminés)
def rna_to_prot(rna):
    # Dictionnaire de correspondance des codons ARN aux acides aminés
    codon_tab = {
        "UUU": "Phe",
        "UUC": "Phe",
        "UUA": "Leu",
        "UUG": "Leu",
        "CUU": "Leu",
        "CUC": "Leu",
        "CUA": "Leu",
        "CUG": "Leu",
        "AUU": "Ile",
        "AUC": "Ile",
        "AUA": "Ile",
        "AUG": "Met",
        "GUU": "Val",
        "GUC": "Val",
        "GUA": "Val",
        "GUG": "Val",
        "UCU": "Ser",
        "UCC": "Ser",
        "UCA": "Ser",
        "UCG": "Ser",
        "CCU": "Pro",
        "CCC": "Pro",
        "CCA": "Pro",
        "CCG": "Pro",
        "ACU": "Thr",
        "ACC": "Thr",
        "ACA": "Thr",
        "ACG": "Thr",
        "GCU": "Ala",
        "GCC": "Ala",
        "GCA": "Ala",
        "GCG": "Ala",
        "UAC": "Tyr",
        "UAU": "Tyr",
        "UAA": "*",
        "UAG": "*",
        "CAU": "His",
        "CAC": "His",
        "CAA": "Gln",
        "CAG": "Gln",
        "AAU": "Asn",
        "AAC": "Asn",
        "AAA": "Lys",
        "AAG": "Lys",
        "GAU": "Asp",
        "GAC": "Asp",
        "GAA": "Glu",
        "GAG": "Glu",
        "UGU": "Cys",
        "UGC": "Cys",
        "UGA": "*",
        "UGG": "Trp",
        "CGU": "Arg",
        "CGC": "Arg",
        "CGA": "Arg",
        "CGG": "Arg",
        "AGU": "Ser",
        "AGC": "Ser",
        "AGA": "Arg",
        "AGG": "Arg",
        "GGU": "Gly",
        "GGC": "Gly",
        "GGA": "Gly",
        "GGG": "Gly",
    }

    proteins = []
    for i in range(0, len(rna), 3):
        codon = rna[i : i + 3]
        if len(codon) != 3:
            break  # stop the transcription at the end

        amino_acid = codon_tab[codon]
        if amino_acid == "*":
            break  # stop the transcription on a stop codon

        proteins.append(amino_acid)

    return proteins


# Calculer le complément inverse de la chaîne ADN
def invert_dna(dna):
    dna_inv = ""
    for b in dna:
        if b == "A":
            dna_inv += "T"
        elif b == "T":
            dna_inv += "A"
        elif b == "C":
            dna_inv += "G"
        elif b == "G":
            dna_inv += "C"

    return dna_inv


# Calculer le taux de GC de la séquence ADN
def gc_in_dna(dna):
    num_gc = 0
    for b in dna:
        if b in ["C", "G"]:
            num_gc += 1

    return (num_gc / len(dna)) * 100


# Calculer les fréquences de codons dans la chaîne ADN
def freq_codon(dna):
    prot = rna_to_prot(dna_to_rna(dna))
    d = {}
    for b in prot:
        if b in d:
            d[b] += 1
        else:
            d[b] = 1

    return d


# Réaliser des mutations aléatoires sur la chaîne ADN
def dna_mutation(dna, num):
    mut_dna = dna
    mut_index = random.sample(range(0, len(dna)), num)

    print(f"Mutation indexes : {mut_index}")
    for m in mut_index:
        mut_dna = mut_dna[:m] + random.choice(["A", "T", "C", "G"]) + mut_dna[m + 1 :]

    return mut_dna


# Chercher un motif dans la chaîne ADN
def search_motif(dna, motif):
    positions = []

    for i in range(len(dna) - len(motif) + 1):
        if dna[i : i + len(motif)] == motif:
            positions.append(i + 1)

    return positions


# Générer la chaîne ADN consensus et la matrice profil
""" --- function here --- """

# ------------------------------------------------------------------------------------------------#
# Main
# ------------------------------------------------------------------------------------------------#
# DNA = "SATCGGCTAGATCGATCGTCGCTA"

print("enter number : ", end="")
n = input()

dna = creat_random_dna(int(n))
print(f"DNA : {dna}")
print()


if is_dna_valid(dna):
    print("The DNA is valid\n")
else:
    quit("Invalid DNA")


print(f"Nucleic bases frequences : {base_freq(dna)}\n")


rna = dna_to_rna(dna)
print(f"RNA : {rna}\n")


print(f"proteins sequence : {rna_to_prot(rna)}\n")


print(f"Inverted DNA : {invert_dna(dna)}\n")


print(f"frequency of GC in DNA : {gc_in_dna(dna)}\n")


print(f"Codon frequences : {freq_codon(dna)}\n")


print("enter number of mutations : ", end="")
m = input()
print(f"DNA after mutations : {dna_mutation(dna, int(m))}\n")


print("enter motif : ", end="")
motif = input()
pos = search_motif(dna, motif)
if len(pos) == 0:
    print(f"Motif '{motif}' was not found in DNA\n")
else:
    print(f"Motif positions : {pos}\n")
