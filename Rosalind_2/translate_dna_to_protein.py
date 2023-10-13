#First: translate DNA to RNA
import bio_tables#The codon table is saved here
def dna_to_rna(dna_seq):
    rna = ''
    for i in dna_seq:
        if i == "T":
            rna += "U"
        else:
            rna += i
    return rna
codon_table = bio_tables.Table().codon_table()
#Convert rna to protein
def rna_to_protein(rna):
    n = 0
    protein_ = []
    stop_codons = ["UAA", "UAG", "UGA"]
    while n < len(rna) - 2:
        codon = rna[n:n + 3]
        if codon in stop_codons:
            return "".join(protein_)
        else:
            if codon in codon_table:
                protein_.append(codon_table[codon])
        n += 3
    return "".join(protein_)



