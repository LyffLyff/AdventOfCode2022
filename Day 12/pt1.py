# https://adventofcode.com/2022/day/12


f = open("input.txt", "r")
input : str = f.read()
f.close()

print(input)

# Dijkstra’s Shortest Path Algorithm
visited_nodes : dict = {} #index in input : steps from start
unvisisted_nodes : list = []

current_position : int = 0
ROWS : int = len(input.split('\n')) + 3

# init nodes lists
for i in range(len(input)):
  if input[i] != "S":
    unvisisted_nodes.append(i)
  else:
    visited_nodes[i] = 0
    current_position = i

print("NEXTLINE: ",input[current_position + ROWS + ROWS + 1])

# get possible positions
for i in range(len(input) - 1):
	if ord(input[i + 1]) < ord(input[i]):
		unvisisted_nodes.append(i + 1)

# find paths
for i in range(len(input)):
  if input[current_position] == "S":
    print("Start Go wherever")
  elif ord(input[current_position + 1]) < ord(input[current_position]):
    # checking left
    current_position += 1
    visited_nodes[current_position] = 1
    unvisisted_nodes.pop(current_position)
  elif ord(input[current_position + ROWS]) < ord(input[current_position]):
    pass



print(visited_nodes)