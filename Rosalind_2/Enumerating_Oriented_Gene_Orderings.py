def signed_permutations(arr):
    if len(arr) == 0:
        return [[]]

    subproblem = arr[1:]
    sub_permutations = signed_permutations(subproblem)
    result = []

    for perm in sub_permutations:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + [arr[0]] + perm[i:]
            result.append(new_perm)
            if arr[0] != 0:
                new_perm = perm[:i] + [-arr[0]] + perm[i:]
                result.append(new_perm)

    return result


def write_signed_permutations_to_file(arr, filename):
    signed_perms = signed_permutations(arr)
    with open(filename, 'w') as file:
        file.write(str(len(signed_perms))+"\n")
        for perm in signed_perms:
            file.write(' '.join(map(str, perm)) + '\n')

n = 5
input_arr = list(range(1,n+1))
print(input_arr)
output_file = "signed_permutations.txt"
write_signed_permutations_to_file(input_arr, output_file)
