#read the file
with open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day5.txt','r') as f:
    t=f.read()
    lines=f.readlines()

#print(t)

#split range and list
t_range,t_list=t.split('\n\n')
id_range = t_range.split('\n')
id_list=t_list.split('\n')
#print(id_range)

count=0
for i in id_list:
    fresh=False
    for rg in id_range:
        s,e=rg.split('-')
        if int(i) in range(int(s),int(e)+1):
            fresh=True
    if fresh==True:
        count+=1

print("part 1:", count)

num_range_list=[]
for i in id_range:
    a=int(i.split('-')[0])
    b=int(i.split('-')[1])
    num_range_list.append([a,b])
num_range_list.sort()

new_range=[num_range_list[0]]

for compare_item in num_range_list[1:]:
    #print("range to compare is",rg)
    compare_start=compare_item[0]
    compare_end=compare_item[1]
    checked=False
    j=0
    while checked==False:
        for standard in new_range:
            #print("compare with range",n)
            if compare_start in range(standard[0],standard[1]+1):#if overlap
                standard[1]=max(standard[1],compare_end)
                checked=True
        if checked==False:
            new_range.append([compare_start,compare_end])
            checked=True
    #print("new range")

print(new_range)

count2=0
for f in new_range:
    inter=f[1]-f[0]+1
    count2+=inter
            
print("part 2:",count2)
