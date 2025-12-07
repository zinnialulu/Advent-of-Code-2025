#read the file
file=open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day7.txt','r')
lines=file.readlines()
y=len(lines)
m=[]
q=[]
for line in lines:
    line = line.rstrip()
    l=list(i for i in line)
    m.append(l)
    lineq=line.replace('.',str(0))
    lq=list(i for i in lineq)
    q.append(lq)
#print(m)

x=len(m[0])

beam_start=m[0].index('S')
m[1][beam_start]='|'
q[1][beam_start]=1



for i in range(1,y-1):
    for j in range(x-1):
        if m[i][j]=='|':
            if m[i+1][j]=='.':
                m[i+1][j]='|'
                q[i+1][j]=int(q[i+1][j])+int(q[i][j])
            elif m[i+1][j]=='^':
                m[i+1][j-1]='|' #left side
                q[i+1][j-1]=int(q[i+1][j-1])+int(q[i][j])                    

                m[i+1][j+1]='|' #right side
                q[i+1][j+1]=int(q[i+1][j+1])+int(q[i][j])
            elif m[i+1][j]=='|':
                q[i+1][j]=int(q[i+1][j])+int(q[i][j])

    
    
count=0
for i in range(1,y-1):
    for j in range(x-1):
         if m[i][j]=='^' and m[i-1][j]=='|':
             count+=1
print("p1 answer is:", count)

count2=1
for i in range(x):
    count2+=int(q[-1][i])
print("p2 answer is:", count2)