#Create a probability table
""""AAAA",1,"AAAa":1,
"AAaa":1, "AaAa":0.75, "Aaaa":0.5,
"aaaa":0]"""
table = [1,1,1,0.75,0.5,0]
def expected_offsprings(dataset):
    """The dataset is a list"""
    expected = 0
    for i in range(len(dataset)):
        temp = int(dataset[i])*table[i]
        expected += temp
    return expected*2
if __name__ == "__main__":
    test_2 = [17149, 20000, 17499, 16272, 17821, 17393]
    test_2_result = expected_offsprings(test_2)
    print(test_2_result)
