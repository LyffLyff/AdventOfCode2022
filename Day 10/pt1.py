# https://adventofcode.com/2022/day/10

SIGNAL_STRENGTH_CHECKS : list = [20, 60, 100, 140, 180, 220]
ADD_CMD_CYCLES : int = 2
cycle_counter : int = 0
signal_strength_sum : int = 0
values : list = []

input = open("input.txt", "r").read().splitlines()

def increment_cycle() -> None:
	global cycle_counter
	global signal_strength_sum
	cycle_counter += 1
	if cycle_counter in SIGNAL_STRENGTH_CHECKS:
		print((1 + sum(values)))
		print(values)
		signal_strength_sum += (1 + sum(values)) * cycle_counter

for i in range(len(input)):
	command : list = input[i].split(" ")
	match command[0]:
		case "noop":
			increment_cycle()
		case "addx":
			for i in range(ADD_CMD_CYCLES):
				increment_cycle()
			values.append(int(command[1]))

print(signal_strength_sum)