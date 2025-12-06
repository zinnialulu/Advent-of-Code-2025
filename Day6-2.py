#read the file
import re

file=open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day6.txt','r')
content=file.readlines()
#print(content)
x=len(content)
input=[]
for lines in content:
    #input.append
    line=lines.rstrip('\n')
    #print(line)
    input.append(line)
#print(input)

y=len(input[0])
math=[]
for j in range(y):
    s=""
    for i in range(x):
        s+=input[i][j]
    #print(s)
    math.append(s)
#print(math)

sum=0
ans1=0
ans2=1
op='reset'
for item in math:
    #print(item)
    if not re.search(r'\d',str(item)):
        #if there is no number it is a separation column
        #print("seperation")
        op='reset'
    elif str(item)[-1]=="+":
        op='plus'
        item=item[:-1]
        #print("plus",item)
    elif str(item)[-1]=="*":
        op='mul'
        item=item[:-1]
        #print("mul",item)
    if op=='reset':
        sum+=max(ans1,ans2)
        #print(sum)
        ans1=0
        ans2=1
    else:
        if op=='plus':
            ans1+=int(item)
        if op=='mul':
            ans2*=int(item)
sum+=max(ans1,ans2)        
print(sum)