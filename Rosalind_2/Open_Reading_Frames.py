#Idea:
#Step 1: find all reading frames
#Step 2: find all "OPEN" reading frames (need to divide each reading frames into codons first!
#Step 3: translate all open readig frames into RNA
#Step 4: translate all "valid" RNA into protein
from reverse_complement import reverse_complement as rc#To get reverse complement from a dna sequence

def get_codons(seq):
    """This function help to separate a dna/rna sequence into codons (3 nycleotides)
    Input: sequence"""
    all_codons = []
    k = 0
    while k < len(seq) - 2:
        temp = seq[k:k+3]
        all_codons.append(temp)
        k += 3
    return all_codons

def all_reading_frames(dna_seq):
    """To find 6 total reading frames from a seq
    Input: a dna_seq
    Output: a list of all reading frames (list) as codons"""
    length = len(dna_seq)
    all_rf = []
    original_frames = [dna_seq[k:length-k+1] for k in range(3)]
    reverse_strand = rc(dna_seq)
    all_rf = original_frames.copy()
    reverse_strand_frames = [reverse_strand[k:length-k+1] for k in range(3)]
    #for i in original_frames:
    #    all_rf.append(rc(i))
    all_rf.extend(reverse_strand_frames)
    #print(all_rf)
    all_rf_as_codons = []
    for i in all_rf:
        all_rf_as_codons.append(get_codons(i))
    return all_rf_as_codons

def orf(dna_seq):
    # The start codon
    start_codon = "ATG"
    stop_codon = ["TAG", "TGA", "TAA"]
    temp_orfs = []
    """Input: only 1 dna sequence"""
    current_position = 0
    length = len(dna_seq)
    while current_position < length:
        for i in range(current_position, length):
            if dna_seq[i] == start_codon:
                start = i
                for j in range(start, length):
                    if dna_seq[j] in stop_codon:
                        temp = dna_seq[start:j]#j now is a stop position
                        temp_orfs.append(temp)
                        current_position = current_position + j
                        #print("current: ", current_position)
                        break
        current_position += 1
    return temp_orfs

def all_orfs(dna_seq):
    # First: find all reading frames
    all_dna_reading_frames = all_reading_frames(dna_seq)
    # Second: find all orfs
    all_orfs = []
    for i in all_dna_reading_frames:
        # print("i = ",i)
        temp = orf(i)
        # print("temp = ", temp)
        for current_temp in temp:
            if current_temp not in all_orfs:
                all_orfs.append(current_temp)
    #Then we translate all the open reading frames into RNA:
    """
    all_rnas = []
    for i in all_orfs:
        temp = translate_dna_to_protein.dna_to_rna(i)
        all_rnas.append(temp)
    #Then we translate all rna to protein
    all_protein = []
    for i in all_rnas:
        temp = translate_dna_to_protein.rna_to_protein(i)
        if temp not in all_protein:
            all_protein.append(temp)
    print(all_orfs)
    return all_protein"""
    return all_orfs
def from_dna_to_rna(dna):
    "Input: dna list as codons"
    rna = []
    for codon in dna:
        temp_codon = ''
        for j in codon:
            if j == "T":
               temp_codon += "U"
            else:
               temp_codon += j
        rna.append(temp_codon)
    return rna
#Convert rna to protein
import bio_tables#To get the codon table
def rna_to_protein(rna):
    codon_table = bio_tables.Table().codon_table()
    n = 0
    protein_ = []
    stop_codons = ["UAA", "UAG", "UGA"]
    while n < len(rna):
        codon = rna[n]
        if codon in stop_codons:
            return "".join(protein_)
        else:
            if codon in codon_table:
                protein_.append(codon_table[codon])
        n += 1
    return "".join(protein_)

def all_proteins(dna):
    """Input: an arbitray dna sequence
    Output: get all possible proteins (not mention introns, exons)"""
    all_rnas = []

    #Get all open reading frames
    all_all_orfs_ = all_orfs(dna)
    # Get the longeset reading frame

    #longest_protein_ = longest_protein(dna)
    longest_protein_ = []
    for i in longest_protein_:
        if i not in all_all_orfs_ and i:
            all_all_orfs_.append(i)
    #all_all_orfs_.append(l)
    for i in all_all_orfs_:
        temp_rna =  from_dna_to_rna(i)
        all_rnas.append(temp_rna)

    all_proteins_list = []
    for i in all_rnas:
        all_proteins_list.append(rna_to_protein(i))


    return all_proteins_list

def longest_protein(dna):
    """Return the longest protein, including the stop codons in between"""
    #Convert to codons

    dna_codons = get_codons(dna)
    # The reverse complement strand
    # Reverse
    reverse_comp_strand = []
    for i in dna_codons:
        temp = ''
        for j in i:
            if j == 'A':
                temp += 'T'
            elif j == 'T':
                temp += 'A'
            elif j == 'G':
                temp += 'C'
            else:
                temp += 'G'
        reverse_comp_strand.append(temp)
    reverse_comp_strand = reverse_comp_strand[::-1]

    #The first strand
    # Longest orf
    start_codon = "ATG"
    stop_codon = ["TAG", "TGA", "TAA"]
    start = 0#Assuming that there is at least a start codon in the sequence
    for i in range(len(dna_codons)):
        if dna_codons[i] == start_codon:
            start = i
            break
    stop = 0
    for i in range(len(dna_codons)):#Find the last occurrence of stop codon
        if dna_codons[i] in stop_codon:
            stop = i
    first_strand = dna_codons[start:stop]
    longest = []
    if first_strand:
        longest.append(first_strand)
    #For the complementary strand
    start = 0  # Assuming that there is at least a start codon in the sequence
    for i in range(len(reverse_comp_strand)):
        if reverse_comp_strand[i] == start_codon:
            start = i
            break
    stop = 0#Assuming that there is at least a start codon in the sequence
    for i in range(len(reverse_comp_strand)):#Find the last occurrence of stop codon
        if reverse_comp_strand[i] in stop_codon:
            stop = i
    second_strand = reverse_comp_strand[start:stop]
    if second_strand not in longest and second_strand:
        longest.append(second_strand)
    return longest
#Convert to rna
#rna_codons = from_dna_to_rna(dna_codons)


if __name__ == "__main__":
    with open(".\dataset\orf.txt", "r") as file:
        file_content3 = file.readlines()
    file_content3 = "".join([x.strip() for x in file_content3])
    #print(file_content3)
    result = all_proteins(file_content3)
    #print(sorted(result,key=len))
    #print(len(test))
    #print(longest_protein(test))
    #print(longest_protein("TAGTAATAATAATAA"))
    with open("orf_test_submit_ok.txt",'w') as file:
        for i in result:
            file.write(i)
            file.write("\n")
