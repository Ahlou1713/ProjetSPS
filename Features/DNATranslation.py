# Traduire une chaîne ARN en protéines
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
