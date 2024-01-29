
#lire le fichier et le decouper en lignes
def read_file_slice_it(path):

    file = open(path, 'r')
    dna_list = file.read().splitlines()

    return dna_list
