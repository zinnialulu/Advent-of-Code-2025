#read the file
file=open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day1.txt','r')
lines=file.readlines()
#print(lines[:5])

num=50
count=0
#convert the string to number, L mean decrease and R means increase
for line in lines:
    x=int(line[1:])
    if x//100>=1:
        count+=x//100
        x=x%100
    #print(f"for line {line} x is {x} and count is now {count}")

    if line[0] == "L": #if turn left
        if (num-x)<=0<num: #check if pass 0
            count+=1
            num=num+100
        num-=x
        num=num%100
        print(f"turn left, new num is {num} and count is now {count}")
    else: #if turn right
        if (num+x)>=100 : #check if pass 0
            count+=1
            num=num-100
        num+=x
        num=num%100
        
        #print(f"turn right, new num is {num} and count is now {count}")
    #print()

print(f"final number is {num}", f"count is {count}")
