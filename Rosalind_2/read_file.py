#We treat the permuation as an anagram problem => use the top-down approach
def create_string(num):
    #signed_str = ["-"+ str(x) for x in range(1,num + 1)]
    unsigned_str = [str(i) for i in list(range(1,num + 1))]
    signed_str = ['-'+str(i) for i in list(range(1, num + 1))]
    signed_str.extend(unsigned_str)
    return signed_str
print(create_string(5))