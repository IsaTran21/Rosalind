import read_fasta
import translate_dna_to_protein as to_pro
path = ".\dataset\splc.txt"
seq = read_fasta.read_fasta_1(path)
#seq = read_fasta.read_fast(path)
#print(seq)
#print(seq)
main_string = seq[0]
introns = seq[1:]
"""
temp_dna = main_string
temp_dna_list = []
k = 1
for sub in substrings_dna:
    index = temp_dna.find(sub)
    if index != -1:
        remove_index = index + len(sub)
        previous_dna = temp_dna[:index]
        temp_dna = temp_dna[remove_index:]
        temp_dna_list.append(previous_dna)
        if k == len(substrings_dna):
            temp_dna_list.append(temp_dna)
        k+=1
    print(index)
clean_dna = "".join(temp_dna_list)
"""
#First: translate dna to rna
for intron in introns:
    main_string = main_string.replace(intron, '')
rna = to_pro.dna_to_rna(main_string)
#rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

#Then: translate rna to protein
pro = to_pro.rna_to_protein(rna)
with open ("rna_splicing.txt","w") as file:
    file.write(pro)
print(pro)