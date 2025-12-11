from collections import deque

with open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day11.txt','r') as file:
    input=file.readlines()
    tree={}
    for line in input:
        line=line.rstrip()
        a,b=line.split(':')
        nodes=b.split()
        tree[a]=nodes

#print(tree)

def find_all_path(t:dict, start:str, target:str,path=[]) -> list:
    path=path+[start]
    if start == target:
        return [path]
    if start not in t:
        return []
    all_path=[]
    for children in t[start]:
        if children not in path:
            newpaths=find_all_path(t,children,target,path)
            for newpath in newpaths:
                all_path.append(newpath)
    return all_path


print(len(find_all_path(tree,'you','out')))

p2=find_all_path(tree,'svr','out')
c2=0
for i in p2:
    if 'dac' in i and 'fft' in i:
        c2+=1
print(c2)