import re
def read_fast(path):
    with open(path, "r") as file:
        sequence = []
        for line in file:
            # Skip header lines starting with '>'
            if line.startswith(">"):
                continue
            # Remove any leading/trailing whitespace and append the line to the sequence
            #sequence += line.strip()
            sequence.append(line.strip())

    # Now, 'sequence' contains the DNA, RNA, or protein sequence from the FASTA file
    return sequence

def read_fasta_1(path):
    """Used for RNA_Splicing"""
    with open(path, 'r') as file:
        lines = file.readlines()

    def get_sequence(sep):
        sep = "".join(sep)  # because the sep is a list
        return sep

    # Define a regular expression pattern to match "Rosalind_xxxx" where 'xxxx' is a number between 0000 and 9999
    pattern = r'>Rosalind_(\d{1,4}|[0-9]{1,4}|[0-9]{1,3}[0-9]{1,3}|[0-9]{1,2}[0-9]{1,2}[0-9]{1,2}|[0-9]{1,1}[0-9]{1,1}[0-9]{1,1}[0-9]{1,1})\n'
    #pattern = r'>Rosalind_\d{2}'
    all_labels = []
    for line in lines:
        if re.match(pattern, line):
            all_labels.append(line)

    # seperate
    lines_1 = lines.copy()
    dna_string = []

    for j in range(len(all_labels)):

        sep = []
        for i in range(1, len(lines_1)):
            if lines_1[i] not in all_labels:
                sep.append(lines_1[i].strip())
            else:
                end = i
                del lines_1[0:i]
                break
        dna_string.append(
            [all_labels[j][1:].rstrip(), get_sequence(sep)])  # get the label with its corresponding sequence
    target = [i[1] for i in dna_string]
    return target
if __name__ == "__main__":
    path = ".\dataset\splc.txt"
    test = read_fasta_1(path)
    print(test)
