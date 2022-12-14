# https://adventofcode.com/2022/day/9

import re
import numpy

input = open("input.txt", "r").read().splitlines()

start_pos : list = [0,0]
head_grid_pos_x : int = start_pos[0]
head_grid_pos_y : int = start_pos[1]
tail_grid_pos_x : int = start_pos[0]
tail_grid_pos_y : int = start_pos[1]
unique_positions_head : list = []
unique_positions_tail : list = []


def move_grid_entity(grid_entity : list, direction : str) -> list:
	match direction:
		case 'R':
			grid_entity[0] += 1
		case 'L':
			grid_entity[0] -= 1
		case 'D':
			grid_entity[1] += 1
		case 'U':
			grid_entity[1] -= 1
	return grid_entity 


def move_tail(head_pos : list, tail_pos : list) -> list:
	if abs(head_pos[1] - tail_pos[1]) > abs(head_pos[0] - tail_pos[0]):
		tail_pos[0] += numpy.sign(head_pos[0] - tail_pos[0])
	if abs(head_pos[0] - tail_pos[0]) > abs(head_pos[1] - tail_pos[1]):
		tail_pos[1] += numpy.sign(head_pos[1] - tail_pos[1])
	# moving x
	if abs(head_pos[0] - tail_pos[0]) > 1:
		tail_pos[0] += numpy.sign(head_pos[0] - tail_pos[0])
	# moving y
	if abs(head_pos[1] - tail_pos[1]) > 1:
		tail_pos[1] += numpy.sign(head_pos[1] - tail_pos[1])

	return tail_pos


# move head and tail
for i in range(len(input)):
	steps : int = int(re.findall(r'\d+', input[i])[0])
	direction : str = input[i][0]
	for i in range(steps):
		
		# head position
		[head_grid_pos_x, head_grid_pos_y] = move_grid_entity([head_grid_pos_x, head_grid_pos_y], direction)
		if [head_grid_pos_x, head_grid_pos_y] not in unique_positions_head:
			unique_positions_head.append([head_grid_pos_x,head_grid_pos_y])
		
		#calc tail position
		[tail_grid_pos_x, tail_grid_pos_y] = move_tail([head_grid_pos_x,head_grid_pos_y], [tail_grid_pos_x, tail_grid_pos_y])
		print([tail_grid_pos_x, tail_grid_pos_y])
		
		if [tail_grid_pos_x, tail_grid_pos_y] not in unique_positions_tail:
			unique_positions_tail.append([tail_grid_pos_x, tail_grid_pos_y])
		

# filter
print("FINAL HEAD POSITION: ", [head_grid_pos_x, head_grid_pos_y])
print("UNIQUE POSITIONS HEAD: ", unique_positions_head)
print("THE HEAD VISITED SO MANY UNIQUE POSITIONS: ", len(unique_positions_head))
print("THE TAIL VISITED SO MANY UNIQUE POSITIONS: ", len(unique_positions_tail))
print("UNIQUE POSITIONS TAIL: ", unique_positions_tail)
