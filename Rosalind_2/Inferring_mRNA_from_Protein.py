"""Idea:
(a a≡b mod n  and c≡d mod n, then a+c≡b+d mod n and  a×c≡b×d mod n
 for example: if we want to know 2^20 mod 1000 (just for illustration)
 2^10 mod 1000 = 1000 x 1 + 24 => 2^10 ≡ 24 mod 1000 = 24
 we can apply the above formula:
 => a: 2^10, b: 24; c: 2^10, d: 24 => axc ≡ bxd mod n, we don't know the answer for axc, but we know bxd  mod 1000
 = 24x24 mod 1000 = 576
 A maximum 4 codons can code 1 acid amin => divide the list into 10 acid amin at at time and mod 1000000
 => find each congruent of each 10 acid amin => and find the final result
 int corresponds to long in Python 2, and this type has no maximum or minimum limit.
 sys.maxsize is not the maximum value of int; you can handle larger values as long as there is available memory.
 => my current system is 64-bit => divide the list into 100 acid amin at at time instead of 10
"""
freq_table = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'B': 3
}
#B represents the stop codons (3)
def infer_mRNA_from_pro(aa_seq):
    #Devide the aa_seq to 10
    divide_list = []
    c = 0
    while c < len(aa_seq):
        if c + 200 > len(aa_seq):
            temp = aa_seq[c:] + "B"
            divide_list.append(temp)
            break
        else:
            temp = aa_seq[c:c+200]
            divide_list.append(temp)
            c += 200
    all_congruent = []
    for i in divide_list:
        temp = find_modulo(i) % 1000000
        all_congruent.append(temp)
    indirect_result = 1
    for i in all_congruent:
        indirect_result *= i
    result = indirect_result % 1000000
    return result
def find_modulo(aa_seq):
    """To find the b,d in the previous formula"""
    result = 1
    for i in aa_seq:
        result *= freq_table[i]
    return result


if __name__ == "__main__":
    with open("rosalind_mrna.txt", "r") as file:
        content = file.readline()
    print(content.strip())
    test = infer_mRNA_from_pro(content.strip())
    print(test)
