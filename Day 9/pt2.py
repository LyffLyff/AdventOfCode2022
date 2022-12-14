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
body : dict = {}
unique_positions_tail : list = []

print(body)

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


def move_body(guiding_piece : list, following_pos : list) -> list:
	if abs(guiding_piece[1] - following_pos[1]) > abs(guiding_piece[0] - following_pos[0]):
		following_pos[0] += numpy.sign(guiding_piece[0] - following_pos[0])
	if abs(guiding_piece[0] - following_pos[0]) > abs(guiding_piece[1] - following_pos[1]):
		following_pos[1] += numpy.sign(guiding_piece[1] - following_pos[1])
	# moving x
	if abs(guiding_piece[0] - following_pos[0]) > 1:
		following_pos[0] += numpy.sign(guiding_piece[0] - following_pos[0])
	# moving y
	if abs(guiding_piece[1] - following_pos[1]) > 1:
		following_pos[1] += numpy.sign(guiding_piece[1] - following_pos[1])

	return following_pos


for i in range(8):
	body[i] = [0,0]


# move head and tail
for i in range(len(input)):
	steps : int = int(re.findall(r'\d+', input[i])[0])
	direction : str = input[i][0]
	for k in range(steps):
		for j in range(10):
			match j:
				case 0:
					# head position
					[head_grid_pos_x, head_grid_pos_y] = move_grid_entity([head_grid_pos_x, head_grid_pos_y], direction)
				case 9:
					#calc tail position
					[tail_grid_pos_x, tail_grid_pos_y] = move_body(body.get(7), [tail_grid_pos_x, tail_grid_pos_y])
						
					if [tail_grid_pos_x, tail_grid_pos_y] not in unique_positions_tail:
						unique_positions_tail.append([tail_grid_pos_x, tail_grid_pos_y])
				case 1:
					# calc first body position
					move_body([head_grid_pos_x, head_grid_pos_y], body.get(0))
				case _:
					# calc rest body positions
					body[j - 1] = move_body(body.get(j - 2), body.get(j - 1))

		
# filter
print("BODY: ", body)
print("FINAL HEAD POSITION: ", [head_grid_pos_x, head_grid_pos_y])
print("FINAL TAIL POSITION: ", [tail_grid_pos_x, tail_grid_pos_y])
print("UNIQUE POSITIONS HEAD: ", unique_positions_head)
print("THE HEAD VISITED SO MANY UNIQUE POSITIONS: ", len(unique_positions_head))
print("UNIQUE POSITIONS TAIL: ", unique_positions_tail)
print("THE TAIL VISITED SO MANY UNIQUE POSITIONS: ", len(unique_positions_tail))
