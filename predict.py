import sys
import pickle


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.condition = -1

def Build_table(lines):
    table = []
    count = 1
    for line in lines:  # get the data from file
        tmp = []
        c_1 = False
        c_2 = False
        c_3 = False
        c_4 = False
        c_5 = False
        c_6 = False
        c_7 = False
        total = 0
        for word in line.strip().split(" "):
            total += len(word)
            if word.lower() == "de" or word.lower() == "het":
                c_2 = True
            if word.lower() == "a" or word.lower() == "an":
                c_3 = True
            if len(word) > 10:
                c_4 = True
            if word.startswith('s'):
                c_5 = True
            if word.find("ed")!=-1:
                c_6 = True
            if word == "the" or word == "and" or word == "so":
                c_7 = True
        if (total/len(line.strip().split(" ")) > 5):
            c_1 = True
        tmp = [c_1, c_2, c_3, c_4, c_5,c_6,c_7,count]
        count+=1
        table.append(tmp)
    return table

def split_table(table,split_point):
    true_table = []
    false_table = []
    for i in table:
        if i[split_point] == True:
            true_table.append(i[:split_point] + i[(split_point + 1):])
        else:
            false_table.append(i[:split_point] + i[(split_point + 1):])
    return true_table,false_table

def dt_predict(root,content,result):
    split_point = root.condition
    if content == []:
        return 
    # print(root.data)
    # print(content)
    if split_point == -1:
        class_type = root.data[0][len(root.data[0])-1]
        for i in content:
            last = i[len(i)-1]
            result.append([last,class_type])
    if split_point != -1:
        true_table,false_table = split_table(content,split_point)
    
    if root.left:
        dt_predict(root.left,true_table,result)
    if root.right:
        dt_predict(root.right,false_table,result)
    return 

def ada_boost_predict(table,z):
    result = []
    for i in table:
        prediction = []
        for hy in range(0,len(z)):
            tmp = []
            if i[hy] == True:
                tmp.append("nl")
            if i[hy] == False:
                tmp.append("en")
            tmp.append(z[hy])
            prediction.append(tmp)
        nl_vote = 0
        en_vote = 0
        for p in prediction:
            if p[0] =="nl":
                nl_vote += p[1]
            if p[0] =="en":
                en_vote += p[1]
        if nl_vote > en_vote:
            result.append("nl")
        else :
            result.append("en")
    
    return result







data_set = pickle.load( open( sys.argv[1], "rb" ) )
condition = data_set[1]
z = data_set [2]
root = data_set[0]


with open(sys.argv[2]) as f:
    lines = f.readlines()

    
if condition == "dt":
    table = Build_table(lines)
    result = []
    dt_predict(root,table,result)
    result.sort(key=lambda x: x[0])
    for i in range(0,len(result)):
        print(result[i][1])

if condition =="ada":
    table = Build_table(lines)
    result = ada_boost_predict(table,z)
    for i in range(0,len(result)):
        print(result[i])