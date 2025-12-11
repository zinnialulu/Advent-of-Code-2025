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


print("part 1:", len(find_all_path(tree,'you','out')))

###part 2 svr to out is too big

#check svr to dac
tree2={i:j for i,j in tree.items() if (i!='fft')and (i!='out')}
svr_to_dac=find_all_path(tree2,'svr','dac')
print("from svr to dac:",len(svr_to_dac))


#check svr to fft
tree2={i:j for i,j in tree.items() if (i!='dac')and (i!='out')}
svr_to_fft=find_all_path(tree2,'svr','fft')
print("from svr to fft:",len(svr_to_fft))


#check between dac and fft
tree2={i:j for i,j in tree.items() if (i!='svr')and (i!='out')}
dac_to_fft=find_all_path(tree2,'dac','fft')
fft_to_dac=find_all_path(tree2,'fft','dac')
print("from dac to fft:",len(dac_to_fft))
print("from fft to dac:",len(fft_to_dac))

#check dac to out
tree2={i:j for i,j in tree.items() if (i!='svr')and (i!='ffc')}
dac_to_out=find_all_path(tree2,'dac','out')
print("from dac to out:",len(dac_to_out))

#check fft to out
tree2={i:j for i,j in tree.items() if (i!='svr')and (i!='dac')}
fft_to_out=find_all_path(tree2,'fft','out')
print("from fft to out:",len(fft_to_out))

#svr to dac to fft to out
l1=len(svr_to_dac)*len(dac_to_fft)*len(fft_to_out)
l2=len(svr_to_fft)*len(fft_to_dac)*len(dac_to_out)

print(l1+l2)