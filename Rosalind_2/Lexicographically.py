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

    test = "A B C D E F G H"

    test_data = test.split(" ")

    test_result_all = lexico_all(test_data,3)
    final = sorted(test_result_all)
    with open("lexico.txt", "w") as file:
        for i in final:
            file.write(i)
            file.write("\n")

