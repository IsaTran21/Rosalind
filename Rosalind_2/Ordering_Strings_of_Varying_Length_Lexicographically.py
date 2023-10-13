#Ordering Strings of Varying Length Lexicographically
def lexico(arr,level):
    if level == 1:
        return arr[0]
    subproblem = lexico(arr, level - 1)
    result = []
    for i in range(len(subproblem)):
    #for i in range(l):
        for j in arr:
            temp = subproblem[i]
            temp += j
            result.append(temp)
    return result
def lexico_all(arr_,level):
    result = []
    arr = arr_.copy()
    all_list = [[i] for i in arr]
    for i in range(len(arr)):
        for j in range(len(arr)):
           if arr[j] not in all_list[i][0]:
               all_list[i].append(arr[j])
    for i in all_list:
        temp = lexico(i,level)
        result.extend(temp)
    return result

if __name__ == "__main__":

    test = "X M V P B Q H D K W C"

    test_data = test.split(" ")
    result = []

    n = 4
    for i in range(1,n+1):
        test_result_temp = lexico_all(test_data, i)
        result.extend(test_result_temp)
    #final = sorted(result)
    def order_sort(s):
        order = {"X": 0, "M": 1, "V": 2, "P":3, "B":4, "Q":5,"H":6, "D":7, "K":8, "W":9, "C":10}
        return [order[c] for c in s]
    sorted_final = sorted(result, key=order_sort)
    with open("varying_lexico.txt", "w") as file:
        for i in sorted_final:
            file.write(i)
            file.write("\n")

