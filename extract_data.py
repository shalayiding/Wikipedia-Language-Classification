from os import truncate
import sys
from math import fabs, log2
from numpy import log as ln, true_divide
import pickle
import random

with open(sys.argv[1]) as f:
    lines_1 = f.read()


whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
nl_word = lines_1.strip()
nl_word = ''.join(filter(whitelist.__contains__, nl_word))
nl_word_list = nl_word.replace("("," ").replace(")"," ").split(" ")

# print(nl_word_list)
with open(sys.argv[2]) as f:
    lines_2 = f.read()

en_word = lines_2.strip()
en_word = ''.join(filter(whitelist.__contains__, en_word))
en_word_list = en_word.replace("("," ").replace(")"," ").split(" ")


min_len = min(len(en_word_list),len(nl_word_list))

data_set= []

for i in range(0,min_len-14,15):
    
    line = []
    line.append("en|")
    for j in range(0,15):
        line.append(en_word_list[i+j])
    data_set.append(line)
    line = []
    line.append("nl|")
    for j in range(0,15):
        line.append(nl_word_list[i+j])  
    data_set.append(line)

random.shuffle(data_set)




percentage = float(sys.argv[6])

train_size = int(len(data_set) *percentage)
test_size = int(len(data_set) - train_size)
print("total data split rate : "+ str(percentage*100) +" "+ str((1-percentage)*100))
print("number of data to train : " + str(train_size))
print("number of data to test : " + str(test_size))


with open(sys.argv[3], "w") as f:
    for i in range(0,train_size):
        for j in range(0,len(data_set[i])):
            if j == 0:
                f.write(data_set[i][j])
            else :
                f.write(data_set[i][j]+" ")
        f.write("\n")

with open(sys.argv[4], "w") as f:
    for i in range(train_size,len(data_set)):
        for j in range(0,len(data_set[i])):
            if j == 0:
                # print(len(data_set[i]))
                continue
                #f.write(data_set[i][j])
            else :
                f.write(data_set[i][j]+" ")
        f.write("\n")

with open(sys.argv[5], "w") as f:    #result of the train data 
    for i in range(train_size,len(data_set)):
        for j in range(0,len(data_set[i])):
            if j == 0:
                tmp = data_set[i][j][:-1]
                f.write(tmp)
        f.write("\n")


# array = [[1],[2],[3],[4],[5]]
# print(array)
# random.shuffle(array)
# print(array)