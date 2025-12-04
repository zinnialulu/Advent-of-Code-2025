#read the file
file=open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day4.txt','r')
lines=file.readlines()
matrix=[]
for line in lines:
    line=line.rstrip()
    templ=(list(j for j in line))
    templ.insert(0,".")
    templ.append(".")
    matrix.append(templ)
#print(matrix)

xmax=len(matrix[0])-2
ymax=len(matrix)
#print(xmax)
#print(ymax)

#add false edge to matrix
e=[]
for i in range(0,xmax+2):
    e.append(".")
matrix.insert(0,e)
matrix.append(e)
r=1 #removal count
sum=0
#check inner sqaures
while r!=0: #stop when removal =0 meaning no more can retrieve
    count=0
    for y in range(1,ymax+1):
        for x in range(1,xmax+1):
            check=matrix[y-1][x-1]+matrix[y-1][x]+matrix[y-1][x+1]+matrix[y][x-1]+matrix[y][x+1]+matrix[y+1][x-1]+matrix[y+1][x]+matrix[y+1][x+1]
            #print(check)
            if check.count("@") <4 and matrix[y][x]=="@":
                count+=1
                #print(f"position is at {y},{x}")
                matrix[y][x]="."
    r=count
    sum+=count
print(sum)