import requests
# Send an HTTP GET request to the URL
#urls = ["A2Z669", "B5ZC00", "P07204", "P20840"]
with open("protein_motifs.txt",'r') as file:
    all_names = file.readlines()
urls_temp = [i.strip() for i in all_names]
urls = []
for i in urls_temp:
    if "_" in i:
        temp_url = i.split("_")[0]
        urls.append(temp_url)
    else:
        urls.append(i)
print(urls)

"""with open("protein_motifs.txt",'r') as file:
    all_names = file.readlines()
all_names = [i.strip() for i in all_names]"""
content = []
#data = []
for i in range(len(urls)):
    url = f"https://rest.uniprot.org/uniprotkb/{urls[i]}.fasta"
    response = requests.get(url)
    temp_seq = ''
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.text
        temp = data.split("\n")
        pos_ = 0
        flag = False
        for j in range(len(temp)):
            if temp[j] and j == 0:
                content.append([temp[j]])
            else:
                temp_seq += temp[j]
                flag = True
                pos_ = len(content) - 1
        if temp_seq:
            content[pos_].append(temp_seq)
    else:
        print("not found")
def find_name(sp_seq):
    a = sp_seq[0].split(" ")[0]
    sign = "|"
    count = 0
    name = ''
    for i in a:
        if i == sign or count == 2:
            count += 1
        if count > 2:
            name += i
    return name
all_name = []
for i in content:
    all_name.append(find_name(i))
#print(all_name)
#The re library for finding positions
all_pos = []
import re
def find_positions(dna):

    pattern = r'(?=N[^P][ST][^P])'
    # Print the matches and their indices
    matches = [match.start() + 1 for match in re.finditer(pattern, dna)]
    return matches
final_result = []
for i in range(len(content)):
    temp = find_positions(content[i][1])
    final_result.append([all_names[i], temp])
print(final_result)
with open("finding_a_sliced_motif_answer.txt","w") as file:
    for i in range(len(final_result)):
        if final_result[i][1]:
            file.write(final_result[i][0])
            #file.write("\n")
            temp = " ".join([str(j) for j in final_result[i][1]])
            temp = temp.strip()
            file.write(temp)
            file.write("\n")
#print(len(content[0]))
print(content[3][1])
find_positions(content[3][1])
"""
with open("protein_motifs.txt", 'w') as file:
    for i in content:
        file.write(i[0])
        file.write("\n")"""