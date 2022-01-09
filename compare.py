import sys



with open(sys.argv[1]) as f:
    lines_1 = f.read()

result_1 = lines_1.strip().split("\n")

with open(sys.argv[2]) as f:
    lines_2 = f.read()

result_2 = lines_2.strip().split("\n")

if len(result_1) != len(result_2):
    print("result length  is not same ")
    exit(100)

total = len(result_1)
correct = 0
wrong = 0
for i in range(0,len(result_1)):
    if result_1[i] == result_2[i]:
        correct+=1
    else :
        wrong += 1

print("Total data : "+ str(total) + "\nCorrect is : "+str(correct) +
 " Wrong is : " + str(wrong) + " \nPrediction correcness:" + str(round(correct/total *100))+"%")
