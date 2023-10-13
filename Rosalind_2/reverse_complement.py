def reverse_complement(dna):
    reverse_strand = ''
    for i in dna:
        if i == "A":
            reverse_strand += "T"
        elif i == "T":
            reverse_strand += "A"
        elif i == "G":
            reverse_strand += "C"
        else:
            reverse_strand += "G"
    reverse_strand = reverse_strand[::-1]
    return reverse_strand


if __name__ == "__main__":
    test = "ATGCTA"
    #Expected: GCATGCATGCATGCATGCAT
    print(reverse_complement(test))