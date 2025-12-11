#read the file
import collections
import datetime

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
    
    moves = [int(i, 2) for i in available_edge] #transform into 2bit
    start_int = int(start_node, 2)
    target_int = int(target_input, 2)
    
    tot = [(start_int, 0)] # Stores (current_state_integer, path_taken)
    visited = {start_int}

    while tot:
        # Use pop(0) to remove the first element (the "front" of the tot)
        current_state_int, paths = tot.pop(0) 

        for move_int in moves:
            next_state_int = current_state_int ^ move_int #xor
            
            if next_state_int == target_int:
                return paths + 1

            if next_state_int not in visited:
                visited.add(next_state_int)
                tot.append((next_state_int, paths + 1))

    return -1

def joltage_transform(s:str) -> list:
    l=list(int(i) for i in s[1:-1].split(','))
    return l
    
    
    
def shortest_path(joltage_input:list, available_edge:list,n:int) -> int:
    start_node=tuple(0 for i in range(n)) #start node in forme of [0,0,0,...]
    joltage_input = tuple(joltage_input)
    if start_node==joltage_input:
        return 0
    
    moves = [[int(j) for j in i] for i in available_edge] #transform each edge into a list
    
    tot = collections.deque([(start_node, 0)]) # Stores (current_state_integer, paths_taken)
    visited = set([start_node])

    while tot:
        # Use pop(0) to remove the first element (the "front" of the tot)
        current_state, paths = tot.popleft() 

        for move in moves:
            next_state = tuple(current_state[i]+move[i] for i in range(len(current_state)))
            
            if next_state == joltage_input:
                print(f"BAR: {len(tot)=} {len(visited)=}")
                return paths + 1
            elif any(next_state[i] > joltage_input[i] for i in range(len(next_state))):
                continue

            if next_state not in visited:
                visited.add(next_state)
                tot.append((next_state, paths + 1))

    return -1

with open('C:/Users/yingl/OneDrive/Documents/GitHub/Advent-of-Code-2025/day10.txt','r') as file:
    input=file.readlines()
    count=0
    count2=0
    for idx, line in enumerate(input):
        line=line.rstrip()
        a=line.index(']')
        #print(a)
        target_node=line[:a+1]
        target=target_transform(target_node)
        #print("target:",target)
        n_target=len(target)

        b=line.index('{')
        edge=line[a+2:b]
        edge_l=edge_transform(edge,n_target)
        #print(edge)
        #print("Edge list is:",edge_l)
        
        min_path=shortest_path_xor(target,edge_l,n_target)
        #print(min_path)
        count+=min_path
        #print(b)
        
        joltage=line[b:]
        joltage_target=joltage_transform(joltage)
        #print("joltage target:",joltage_target)
        
        min_path_2=shortest_path(joltage_target,edge_l,n_target)
        #print(min_path_2)
        print(f"FOO: {datetime.datetime.now()} line={idx} {min_path_2=}")
        count2+=min_path_2
        #print(joltage)
        #break
print("Total count for part 1:", count)
print("Total count for part 2:", count2)