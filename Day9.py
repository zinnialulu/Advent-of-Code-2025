#read the file

tiles=[]
with open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day9.txt','r') as file:
    input=file.readlines()
    for line in input:
        line=line.rstrip()
        y,x=line.split(',')
        tiles.append((int(y),int(x)))
#print(tiles)

area=0
for i in range(len(tiles)-1):
    for j in range(i+1,len(tiles)):
        x1=tiles[i][1]
        y1=tiles[i][0]
        x2=tiles[j][1]
        y2=tiles[j][0]
        s=(abs(y2-y1)+1)*(abs(x2-x1)+1)
        if s>area:
            area=s
print(area)
        
        