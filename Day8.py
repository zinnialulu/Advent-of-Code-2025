#read the file

nodes=[]
with open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/example.txt','r') as file:
    input=file.readlines()
    for line in input:
        node=[]
        line=line.rstrip()
        for j in line.split(','):
            node.append(int(j))
        nodes.append(tuple(node))
#print("nodes are:", nodes)
xmax=len(nodes)
pairs=[]
dic_pair={}
for i in range(xmax-1):
    x1=nodes[i][0]
    y1=nodes[i][1]
    z1=nodes[i][2]
    for j in range(i+1,xmax):
        x2=nodes[j][0]
        y2=nodes[j][1]
        z2=nodes[j][2]
        d=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2)
        dic_pair[(nodes[i],nodes[j])]=d

#print(dic_pair)

dic_pairs_asc=dict(sorted(dic_pair.items(), key=lambda item:item[1]))
#print(dic_pairs_asc)

0