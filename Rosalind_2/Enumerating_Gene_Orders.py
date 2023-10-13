#We treat the permuation as an anagram problem => use the top-down approach
def create_string(num):
    return "".join([str(x) for x in range(1,num + 1)])
string = create_string(5)
def permutation(ana):
    #Step 1: find the subproblem
    #Now we just need to apply the anagram problem
    subproblem = ana[1:]
    #Step 2: find the base case
    if len(ana) == 1:
        return [ana]
    #Step 3: what to do?
    solve_subproblem = permutation(subproblem)
    temp_perms = []
    digit = ana[0]
    for perm in solve_subproblem:
        for i in range(len(perm)+1):
            temp = perm[:i] + digit + perm[i:]
            temp_perms.append(temp)
    return temp_perms

if __name__ == "__main__":
    test = permutation(string)
    print(len(test))
    with open("Enumerating.txt",'w') as file:
        file.write(str(len(test))+str("\n"))
        for i in sorted(test):
            for j in i:
                file.write(j + " ")
            file.write("\n")

