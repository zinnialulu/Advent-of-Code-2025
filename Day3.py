#read the file
file=open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day3.txt','r')
lines=file.readlines()
sum1=0
sum2=0
for line in lines:
    line=line.rstrip('\n')
    linedg=[int(i) for i in line]
    #print(linedg)
    l=len(linedg)
    a=max(linedg[0:l-1])
    #print(a)
    id_a=linedg.index(a)
    #print(id_a)
    b=max(linedg[id_a+1:l])
    #print(b)
    num1=a*10+b
    #print(num1)
    sum1+=num1
    
    x=max(linedg[0:l-11])
    num2=(10**(12-1))*x
    id=linedg.index(x)
    #print(f"digit is {x},its index is {id}, and number is {num2}")
    for j in range(11,0,-1):
        y=max(linedg[id+1:l-j+1])
        #print(y)
        id=linedg.index(y,id+1)
        num2+=(10**(j-1))*y
        #print(f"new digit is {y}, new index is {id}, and new number is {num2}")
    print(num2)
    sum2+=num2
#print(sum1)
print(sum2)