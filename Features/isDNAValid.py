
# Vérifier la validité de la chaîne ADN
def is_dna_valid(dna):
    return set(dna) <= set("ATCG")