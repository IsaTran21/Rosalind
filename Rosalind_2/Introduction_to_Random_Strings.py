"""Idea: gc_content = 0.287
g = x/2
c = x/2
a = (1-x)/2
t = (1-x)/2
z = a*c*g*a*t*a*c*a*a
=> log10(z)
=> the probability of a sequence = the multiplication of its
corresponding letters.
Note: log10(x⋅y)=log10(x)+log10(y)"""

import math
import numpy as np
#log_base_10 = math.log10(z)
def each_prob(arr,gc_prob):
    G = gc_prob/2
    C = gc_prob/2
    A = (1 - gc_prob)/2
    T = (1 - gc_prob)/2
    result = 0
    for i in arr:
        if i == "G":
            result += math.log10(G)
        elif i == "C":
            result += math.log10(C)
        elif i == "A":
            result += math.log10(A)
        else:
            result += math.log10(T)
    return round(result,3)


def random_strings(arr,gc_list):
    results = []
    for i in gc_list:
        temp = each_prob(arr,i)
        results.append(temp)
    return results

if __name__ == "__main__":

    with open("random_string.txt","r") as file:
        content = file.readlines()
    content = [i.strip() for i in content]
    dna_seq = content[0]
    gc_list = content[1].split(" ")
    gc_list = [float(i) for i in gc_list]
    test = random_strings(dna_seq, gc_list)
    with open("random_string_answer.txt", "w") as file:
        for i in test:
            file.write(str(i))
            file.write(" ")

