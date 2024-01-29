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
    print('The menu:')
    print('1- Vérifier la validité de la chaîne ADN si cette dernière est lue à partir d\'un fichier' +
              '2- Calculer les fréquences des bases nucléiques dans la chaîne ADN' +
              '3- Transcrire la chaîne ADN en une chaîne ARN.' +
              '4- Traduire la chaîne ARN résultante en protéines (i.e., acides aminés)' +
              '5- Calculer le complément inverse de la chaîne ADN' +
              '6- Calculer le taux de GC de la séquence ADN' +
              '7- Calculer les fréquences de codons dans la chaîne ADN' +
              '8- Réaliser des mutations aléatoires sur la chaîne ADN. Une mutation est une modification rare,' +
              'accidentelle ou provoquée, de la séquence nucléotidique de l\'ADN. Il existe plusieurs types' +
              'de mutations ; il vous est demandé d\'implémenter la mutation ponctuelle par substitution.' +
              'Ce type de mutation consiste à remplacer un nucléotide par un autre. Le nombre de' +
              'mutations à réaliser est spécifié par l\'utilisateur' +
              '9- Chercher un motif dans la chaîne ADN' +
              '10- Générer la chaîne ADN consensus et la matrice profil')
    
    menu = input('What do you want to do? (choose from the numbers 1-10): ')
    match menu:
        case 1:
            for i in dna_list:
                if(is_dna_valid(i)):
                    print("DNA sequence valid!")
                else:
                    print("DNA sequence invalid!")
        case 2:
            for i in dna_list:
                if(is_dna_valid(i)):
                    print("For the sequence" + i,base_frequency(i))
                else:
                    print("DNA sequence invalid!")
        case 3:
            rna_list = []
            for i in dna_list:
                if(is_dna_valid(i)):
                    rna = dna_to_rna(i)
                    print("For the sequence" + i,rna)
                    rna_list.append(rna)
                else:
                    print("DNA sequence invalid!")
        case 4:
            if(rna_list):
                for i in rna_list:
                    print("For " + i,rna_to_prot(i))
        case 5:
            for i in dna_list:
                if(is_dna_valid(i)):
                    print("For " + i,complement_dna(i))
        case 6:
            for i in dna_list:
                if(is_dna_valid(i)):
                    print("For " + i,gc_in_dna(i))
        case 7:
            for i in dna_list:
                if(is_dna_valid(i)):
                    print("For " + i,freq_codon(i))
        case 8:
            for i in dna_list:
                if(is_dna_valid(i)):
                    print("For " + i,dna_mutation(i))
        case 9:
            for i in dna_list:
                if(is_dna_valid(i)):
                    print("For " + i,search_motif(i))
        case 10:
            d = consensus_profile_matrix(dna_list)
            print(d)
        

print('Welcome onboard!')
print('This application\'s aim is to give you the possibility to make some changes upon chosen DNA sequences,' 
+ 'the menu will appear after you select one of the two options below: (to choose type 1 or 2)')
print('1- Choose a file from pc for the DNA sequences to analyse')
print('2- Generate random DNA sequences to analyse')

sequence = int(input())

match sequence:
    case 1:
        path = input('The path to your file: ')
        dna_list = read_file_slice_it(path)

        menu(dna_list)
    case 2:
        sequence_number = input('The number of sequences you want: ')
        sequence_length = input('With what length: ')
        i = 0
        dna_list = []
        while(i<sequence_number):
            dna_list.append(generate_random_dna(sequence_length))
        menu(dna_list)

