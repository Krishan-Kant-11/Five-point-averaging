'''This is code for 5 point averaging of a graph, put your value and after finishing type "end", remember first 
two valuesand last two values are not there in the answer list.'''

l = []
temp = None
print("Enter the value and type \"end\" after you finish : ")
while temp != "end":
    temp = input()
    l.append(temp)

l.pop()
print("Five point average readings are : ")
for i in range(len(l) -4):
    avg = (int(l[i]) + int(l[i+1]) + int(l[i+2]) + int(l[i+3]) +int(l[i+4]))/5
    print(avg)
