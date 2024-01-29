
def consensus_profile_matrix(dna):
    consensus = ''
    profile_matrix = [['A'] + ([0] * len(dna[0])), 
                      ['T'] + ([0] * len(dna[0])), 
                      ['G'] + ([0] * len(dna[0])), 
                      ['C'] + ([0] * len(dna[0]))
                    ]
    for i in dna:
        for j in range(0, len(i)):
            if i[j] == 'A':
                profile_matrix[0][j+1] += 1
            elif i[j] == 'T':
                profile_matrix[1][j+1] += 1
            elif i[j] == 'G':
                profile_matrix[2][j+1] += 1
            elif i[j] == 'C':
                profile_matrix[3][j+1] += 1


    for i in range(1, len(dna[0])+1):
        max = profile_matrix[0][i]
        indexMax = 0
        for j in range(1, 4):
            if profile_matrix[j][i] > max:
                max = profile_matrix[j][i]
                indexMax = j
        consensus += profile_matrix[indexMax][0]


    return {'profile_matrix': profile_matrix, 'consensus': consensus}





dna = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 
       'ATGCCATT', 'ATGGCACT']

print(consensus_profile_matrix(dna))