#read the file
file=open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day2.txt','r')
for line in file:
    line = line.strip()
    ranges=line.split(',')
#print(ranges)

p1=0
for rg in ranges:
    se=rg.split('-')
    start=int(se[0])
    end=int(se[1])
    #print(f"start is {start} and end is {end}")
    for i in range(start,end+1,1):
        #print(i)
        l=len(str(i))
        #print(l)
        if l%2==0 and str(i)[:l//2]==str(i)[l//2:]:
            p1+=i
            #print(f"sum is {p1}")

    for j in range(1,l/2+1):
        if l%j==0:#can be repeated
            
            
            
print("sum", p1)