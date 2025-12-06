#read the file
import re

file=open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day6.txt','r')
content=file.readlines()
x=len(content)
math=[]
input=[]
for lines in content:
    line=lines.strip()
    new_line=line.split()
    input.append(new_line)
y=len(input[0])
for i in range(y):
    math.append([])
    temp=[]
    for j in range(x):
        temp.append(input[j][i])
    math[i]=temp
#print(math)

sum=0
for q in math:
    ans1=0
    ans2=1
    for i in range(x-1):
        if q[-1]=="+":
            ans1+=int(q[i])
        else:
            ans2*=q[i]
    a=max(ans1,ans2)
    sum=sum+a

print(sum)