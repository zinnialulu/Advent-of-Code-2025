tiles=[]
x_list=[]
y_list=[]
with open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day9.txt','r') as file:
    input=file.readlines()
    for line in input:
        line=line.rstrip()
        y,x=line.split(',')
        tiles.append((int(y),int(x)))
        x_list.append(int(x))
        y_list.append(int(y))
#print(tiles)
xmin=min(x_list)
xmax=max(x_list)
ymin=min(y_list)
ymax=max(y_list)
print(xmin,xmax)
print(ymin,ymax)