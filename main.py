from Features.DNAComplement import complement_dna
from Features.DNATranscript import dna_to_rna
from Features.DNATranslation import rna_to_prot
from Features.GCQuantity import gc_in_dna
from Features.baseFreq import base_frequency
from Features.codonFreq import freq_codon
from Features.consensus_profileMatrix import consensus_profile_matrix
from Features.isDNAValid import is_dna_valid
from Features.mutation import dna_mutation
from Features.randomDNASeq import generate_random_dna
from Features.readFile_slice_it import read_file_slice_it
from Features.searchMotif import search_motif

def menu(dna_list):
    while True:
        print("\nThe menu:")
        print(
            "1- Vérifier la validité de la chaîne ADN si cette dernière est lue à partir d'un fichier\n"
            + "2- Calculer les fréquences des bases nucléiques dans la chaîne ADN\n"
            + "3- Transcrire la chaîne ADN en une chaîne ARN\n"
            + "4- Traduire la chaîne ARN résultante en protéines (i.e., acides aminés)\n"
            + "5- Calculer le complément inverse de la chaîne ADN\n"
            + "6- Calculer le taux de GC de la séquence ADN\n"
            + "7- Calculer les fréquences de codons dans la chaîne ADN\n"
            + "8- Réaliser des mutations aléatoires sur la chaîne ADN\n"
            + "9- Chercher un motif dans la chaîne ADN\n"
            + "10- Générer la chaîne ADN consensus et la matrice profil\n"
            + "\n0- Exit\n"
        )

        menu = int(input("What do you want to do? (choose from the numbers 1-10): "))
        print()
        match menu:
            case 0:
                break

            case 1:
                for i in dna_list:
                    if is_dna_valid(i):
                        print("DNA sequence is valid!")
                    else:
                        print("DNA sequence invalid!")

                input("\nClick on Enter to continue")

            case 2:
                for i in dna_list:
                    if is_dna_valid(i):
                        print(
                            f"nucleic bases frequency {base_frequency(i)} for DNA : {i}"
                        )
                    else:
                        print("DNA sequence invalid!")

                input("\nClick on Enter to continue")

            case 3:
                rna_list = []
                for i in dna_list:
                    if is_dna_valid(i):
                        rna = dna_to_rna(i)
                        print(f"DNA : {i}  -->  RNA : {rna}")
                        rna_list.append(rna)
                    else:
                        print("DNA sequence invalid!")

                input("\nClick on Enter to continue")

            case 4:
                if rna_list:
                    for i in rna_list:
                        print(f"RNA : {i}  -->  Proteins : {rna_to_prot(i)}")
                else:
                    print("Creat the RNA sequences (action 3) before doing this action")

                input("\nClick on Enter to continue")

            case 5:
                for i in dna_list:
                    if is_dna_valid(i):
                        print(f"DNA : {i}  -->  Inverted : {complement_dna(i)}")

                input("\nClick on Enter to continue")

            case 6:
                for i in dna_list:
                    if is_dna_valid(i):
                        print(f"GC frequency {gc_in_dna(i)} for DNA : {i}")

                input("\nClick on Enter to continue")

            case 7:
                for i in dna_list:
                    if is_dna_valid(i):
                        print(f"Codon frequency {freq_codon(i)} for DNA : {i}")

                input("\nClick on Enter to continue")

            case 8:
                m = int(input("enter number of mutations : "))
                for i in dna_list:
                    if is_dna_valid(i):
                        print(f"DNA : {i}  -->  Mutation : {dna_mutation(i, m)}")

                input("\nClick on Enter to continue")

            case 9:
                motif = input("enter motif : ")
                for i in dna_list:
                    if is_dna_valid(i):
                        pos = search_motif(i, motif)
                        if pos:
                            print(f"Motif '{motif}' was found in {pos} in DNA : {i}")
                        else:
                            print(f"Motif '{motif}' was not found in DNA : {i}")

                input("\nClick on Enter to continue")

            case 10:
                d = consensus_profile_matrix(dna_list)
                print("Profile Matrix")
                for row in d["profile_matrix"]:
                    print(row)
                print("\nConsensus DNA")
                print(d["consensus"])

                input("\nClick on Enter to continue")

            case 11:
                f = open("testfile.txt", "a")

                # 1
                f.write(
                    "1- Vérifier la validité de la chaîne ADN si cette dernière est lue à partir d'un fichier\n"
                )
                for i in dna_list:
                    if is_dna_valid(i):
                        f.write("DNA sequence is valid!\n")
                    else:
                        f.write("DNA sequence invalid!\n")

                # 2
                f.write(
                    "\n2- Calculer les fréquences des bases nucléiques dans la chaîne ADN\n"
                )
                for i in dna_list:
                    if is_dna_valid(i):
                        f.write(
                            f"nucleic bases frequency {base_frequency(i)} for DNA : {i}\n"
                        )
                    else:
                        f.write("DNA sequence invalid!\n")

                # 3
                f.write("\n3- Transcrire la chaîne ADN en une chaîne ARN\n")
                rna_list = []
                for i in dna_list:
                    if is_dna_valid(i):
                        rna = dna_to_rna(i)
                        f.write(f"DNA : {i}  -->  RNA : {rna}\n")
                        rna_list.append(rna)
                    else:
                        f.write("DNA sequence invalid!\n")

                # 4
                f.write(
                    "\n4- Traduire la chaîne ARN résultante en protéines (i.e., acides aminés)\n"
                )
                for i in rna_list:
                    f.write(f"RNA : {i}  -->  Proteins : {rna_to_prot(i)}\n")

                # 5
                f.write("\n5- Calculer le complément inverse de la chaîne ADN\n")
                for i in dna_list:
                    if is_dna_valid(i):
                        f.write(f"DNA : {i}  -->  Inverted : {complement_dna(i)}\n")

                # 6
                f.write("\n6- Calculer le taux de GC de la séquence ADN\n")
                for i in dna_list:
                    if is_dna_valid(i):
                        f.write(f"GC frequency {gc_in_dna(i)} for DNA : {i}\n")

                # 7
                f.write("\n7- Calculer les fréquences de codons dans la chaîne ADN\n")
                for i in dna_list:
                    if is_dna_valid(i):
                        f.write(f"Codon frequency {freq_codon(i)} for DNA : {i}\n")

                # 8
                f.write("\n8- Réaliser des mutations aléatoires sur la chaîne ADN\n")
                m = int(input("enter number of mutations : "))
                for i in dna_list:
                    if is_dna_valid(i):
                        f.write(f"DNA : {i}  -->  Mutation : {dna_mutation(i, m)}\n")

                # 9
                f.write("\n9- Chercher un motif dans la chaîne ADN\n")
                motif = input("enter motif : ")
                for i in dna_list:
                    if is_dna_valid(i):
                        pos = search_motif(i, motif)
                        if pos:
                            f.write(
                                f"Motif '{motif}' was found in {pos} in DNA : {i}\n"
                            )
                        else:
                            f.write(f"Motif '{motif}' was not found in DNA : {i}\n")

                # 10
                f.write("\n10- Générer la chaîne ADN consensus et la matrice profil\n")
                d = consensus_profile_matrix(dna_list)
                f.write("Profile Matrix\n")
                for row in d["profile_matrix"]:
                    f.write(f"{row}\n")
                f.write("\nConsensus DNA\n")
                f.write(d["consensus"])

                f.close()
                print("File created successfully")

                input("\nClick on Enter to continue")


print("Welcome onboard!")
print(
    "This application aims to give you the possibility to make changes upon chosen DNA sequences,"
    + "the menu will appear after you select one of the two options below: (to choose type 1 or 2)\n"
)

print("1- Choose a file from pc for the DNA sequences to analyse")
print("2- Generate random DNA sequences to analyse")

sequence = int(input())

match sequence:
    case 1:
        path = input("Enter the path to your file: ")
        dna_list = read_file_slice_it(path)

        menu(dna_list)
    case 2:
        sequence_number = int(input("The number of sequences you want: "))
        sequence_length = int(input("With what length: "))

        dna_list = []
        for i in range(sequence_number):
            dna_list.append(generate_random_dna(sequence_length))

        menu(dna_list)