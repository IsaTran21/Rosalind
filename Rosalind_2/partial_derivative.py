"""Idea: P(n,k) = n!/(n-k)! = n*(n-1)*...*(n-k+1)
use the a≡b mod n and c≡d mod n => a*c≡b*d mod n"""

def Partial_derivative(n,r):
    upper = n
    lower = (n - r + 1)
    num_list = list(range(lower,upper + 1))
    num_list_divide = []
    k = 0

    while k < len(num_list):
        if k + 15 > len(num_list)-1:
            num_list_divide.append(num_list[k:])
            break
        else:
            temp = num_list[k:k+15]
            num_list_divide.append(temp)
            k += 15
    modulo_list = []
    for i in num_list_divide:
        temp = 1
        for j in i:
            temp *= j
        modulo_list.append(temp % 1000000)

    # Do the above for second time
    k = 0
    modulo_list_divide = []
    while k < len(modulo_list):
        if k + 2 > len(modulo_list)-1:
            modulo_list_divide.append(modulo_list[k:])
            break
        else:
            temp = modulo_list[k:k+2]
            modulo_list_divide.append(temp)
            k += 2
    result_list = []
    for i in modulo_list_divide:
        temp = 1
        for j in i:
            temp *= j
        result_list.append(temp % 1000000)
    result = 1
    for i in result_list:
       result *= i
    return result % 1000000

if __name__ == "__main__":
    #99 8
    test = Partial_derivative(99,8)
    print(test)

