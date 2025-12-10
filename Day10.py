#read the file

def target_transform(s:str) -> str:
    target=""
    l=len(s)
    for i in range(1,l-1):
        if s[i]=='.':
            target+='0'
        else:
            target+='1'
    return target

def edge_transform(s:str,n:int) -> list:
    l=s.split()
    edge_list=[]
    for i in l:
        e='0'*n
        #print(i)
        index_list=i[1:-1].split(',')
        for j in index_list:
            e=e[:int(j)]+'1'+e[int(j)+1:]
        edge_list.append(e)
    return edge_list
            
def shortest_path_xor(target_input:str, available_edge:list,n:int) -> int:
    start_node='0'*n
    if start_node==target_input:
        return 0
    
    moves = [int(el, 2) for el in available_edge]
    start_int = int(start_node, 2)
    target_int = int(target_input, 2)
    
    queue = [(start_int, 0)] # Stores (current_state_integer, steps_taken)
    visited = {start_int}

    while queue:
        # Use pop(0) to remove the first element (the "front" of the queue)
        current_state_int, steps = queue.pop(0) 

        for move_int in moves:
            next_state_int = current_state_int ^ move_int
            
            if next_state_int == target_int:
                return steps + 1

            if next_state_int not in visited:
                visited.add(next_state_int)
                # Use append() to add to the back of the queue
                queue.append((next_state_int, steps + 1))

    return -1



with open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day10.txt','r') as file:
    input=file.readlines()
    count=0
    for line in input:
        line=line.rstrip()
        a=line.index(']')
        #print(a)
        target_node=line[:a+1]
        target=target_transform(target_node)
        print("target:",target)
        n_target=len(target)

        b=line.index('{')
        edge=line[a+2:b]
        edge_l=edge_transform(edge,n_target)
        #print(edge)
        print("Edge list is:",)
        
        min_path=shortest_path_xor(target,edge_l,n_target)
        print(min_path)
        count+=min_path
        #print(b)
        #joltage=line[b:]
        #print(joltage)
print("Total count:", count)