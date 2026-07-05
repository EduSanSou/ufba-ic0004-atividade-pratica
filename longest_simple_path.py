from numpy import random
import time

n = 5 #insert number of nodes
current_distance = 0 #current distance for dfs approach
best_distance = 0
used = [False]*n #initialize list with false values for dfs approach
adjacency_lists = []
source = 0
initial_best_distance = 0 #initial best distance for greedy algorithm
initial_available_list = [] #initial available list for greedy algorithm
for i in range(n): #initialize list values for greedy algorithm
    initial_available_list.append(i)

#contruct path recursively using depth-first search
def dfs_path(u,current_distance,best_distance,used,last_node):
    used[u] = True
    for v in adjacency_lists[u]:
        if(used[v] == False):
            current_distance += distances_matrix[u][v]
            if current_distance > best_distance:
                last_node = v
            best_distance = max(current_distance,best_distance)
            current_distance,best_distance,used,last_node = \
            dfs_path(v,current_distance,best_distance,used,last_node)
            current_distance -= distances_matrix[u][v]
    used[u] = False
    return current_distance,best_distance,used,last_node

#greedy algorithm for get better distance
def greedy_path(index,available_list,best_distance):
    if n==1: #base case
        return 0,[],0
    distance = 0
    available_list.remove(index)
    next_index = index
    for column in range(n):
        if distances_matrix[index][column] > distance and\
        column in available_list:
            distance = distances_matrix[index][column]
            next_index = column
    best_distance += distance
    if available_list != []:
        next_index,available_list,best_distance = \
        greedy_path(next_index,available_list,best_distance)
    return next_index,available_list,best_distance

print("--- COMPLETE GRAPH ---")
#generate complete graph
for node in range(n):
    neighborhood_list = []
    for neighborhood in range(n):
        if node != neighborhood:
            neighborhood_list.append(neighborhood)
    adjacency_lists.append(neighborhood_list)
print("set of adjacency lists:")
print(adjacency_lists)

# generate distances matrix
A = random.randint(1,100,size=(n,n))
B = (A + A.T)/2
for i in range(n):
    for j in range(n):
        if i == j:
            B[i][j] = 0
distances_matrix = B
print("distances matrix:")
print(distances_matrix)

dfs_start_time = time.time()
current_distance,best_distance,used,last_node = \
dfs_path(source,current_distance,best_distance,used,source) # calculate all possible paths from node 0
print("--- RECURSIVE DFS ---")
print("execution time:")
print("%s seconds" % (time.time() - dfs_start_time))
print("source node:")
print(source)
print("destiny node:")
print(last_node)
print("greater distance for recursive dfs:")
print(best_distance)

greedy_start_time = time.time()
last_index,final_available_list,final_best_distance = \
greedy_path(source,initial_available_list,initial_best_distance)
print("--- GREEDY ALGORITHM ---")
print("execution time:")
print("%s seconds" % (time.time() - greedy_start_time))
print("source node:")
print(source)
print("destiny node:")
print(last_index)
#print("final available list:")
#print(final_available_list)
print("greater distance for greedy algorithm:")
print(final_best_distance)