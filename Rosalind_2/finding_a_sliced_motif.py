#a = "ACGTACGTGACG"
#b = "GTA"
import read_fasta
path = ".\dataset\sseq.txt"
seqs = read_fasta.read_fasta_1(path)
positions = []
s = seqs[0]
t = seqs[1:][0]
for i in range(len(t)):
  if positions:
    k = max(positions)
  else:
    k = 0
  for j in range(k,len(s)):
    if t[i] == s[j]:
      pos = j
      positions.append(pos + 1)
      break
#print(seqs)
for i in positions:
  print(i," ",end="")
with open("finding_a_sliced_motif.txt", "w") as file:
  for i in positions:
    file.write(str(i))
    file.write(" ")