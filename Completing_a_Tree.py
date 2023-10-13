with open('rosalind_tree.txt', 'r') as file:
    content = file.readlines()
content = [[i][0] for i in content]
n = int(content[0].strip())
num_edges = content[1:]
result = n - len(num_edges) - 1
print(result)