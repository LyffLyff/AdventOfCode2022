# https://adventofcode.com/2022/day/10

SIGNAL_STRENGTH_CHECKS : list = [20, 60, 100, 140, 180, 220]
ADD_CMD_CYCLES : int = 2
SCREEN_WIDTH : int = 40
SCREEN_HEIGHT : int = 6
cycle_counter : int = 0
draw_counter : int = 0
sprite_pos : int = 1
values : list = []
screen : list = ['.'] * SCREEN_WIDTH * SCREEN_HEIGHT

input = open("input.txt", "r").read().splitlines()

def increment_cycle() -> None:
	global cycle_counter
	screen.append('#')
	draw_position = (cycle_counter % SCREEN_WIDTH)
	#print("SPRTIE: ", sprite_pos)
	if abs(sprite_pos - draw_position) <= 1:
		screen[cycle_counter] = '#'
	cycle_counter += 1

for i in range(len(input)):
	command : list = input[i].split(" ")
	match command[0]:
		case "noop":
			increment_cycle()
		case "addx":
			for i in range(ADD_CMD_CYCLES):
				increment_cycle()
			values.append(int(command[1]))
			sprite_pos = sum(values) + 1


for y in range(SCREEN_HEIGHT):
	for x in range(SCREEN_WIDTH):
		print(screen[draw_counter],end="")
		draw_counter += 1
	print("\n",end="")