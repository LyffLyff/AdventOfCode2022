# https://adventofcode.com/2022/day/14

import re
from pprint import pprint

f = open("input.txt", mode="r")
input = f.read()
f.close()

# splits input by -> , \n, and ,
input = re.split("\n", input)

# split each scanline by x and y
for i in range(len(input)):
  input[i] = re.split(" -> |,", input[i])

print(input)

fixed_rocks_positions : list = []

# interpret scans
x : int = -1
y : int = -1
px : int = -1
py : int = -1
min_y : int = -1 # if lower == the void

for i in input:
  for j in range(0, len(i), 2):
    x = int(i[j])
    y = int(i[j + 1])
    if y > min_y or min_y == -1:
      min_y = y
    if py != -1:
      if py != y:
        if py - y > 0:
          for k in range(y, py + 1, +1):
            if [x, k] not in fixed_rocks_positions:
              fixed_rocks_positions.append([x, k])
        elif py - y < 0:
          for k in range(py, y + 1, +1):
            if [x, k] not in fixed_rocks_positions:
              fixed_rocks_positions.append([x, k])
      elif px != x:
        if px - x > 0:
          for k in range(x, px + 1, +1):
            if [k, py] not in fixed_rocks_positions:
              fixed_rocks_positions.append([k, y])
        elif px - x < 0:
          for k in range(px, x + 1, +1):
            if [k, py] not in fixed_rocks_positions:
              fixed_rocks_positions.append([k, y])
    py = y
    px = x
  px = -1
  py = -1
  x = -1
  y = -1

pprint(fixed_rocks_positions)
print(min_y)

landed_sandcorns : int = 0
start_pos : list = [500, 0]
current_sandcorn_pos : list = start_pos

while True:
  print(current_sandcorn_pos)
  if [current_sandcorn_pos[0], current_sandcorn_pos[1] + 1] not in fixed_rocks_positions:
    # sandcorn moves down
    current_sandcorn_pos = [current_sandcorn_pos[0], current_sandcorn_pos[1] + 1]
  elif [current_sandcorn_pos[0] - 1, current_sandcorn_pos[1] + 1] not in fixed_rocks_positions:
    # sandcorn moves left and down
    current_sandcorn_pos = [current_sandcorn_pos[0] - 1, current_sandcorn_pos[1] + 1]
  elif [current_sandcorn_pos[0] + 1, current_sandcorn_pos[1] + 1] not in fixed_rocks_positions:
    # sandcorn moves right and down
    current_sandcorn_pos = [current_sandcorn_pos[0] + 1, current_sandcorn_pos[1] + 1]
  else:
    # sandcorn in fixed position
    fixed_rocks_positions.append(current_sandcorn_pos)
    current_sandcorn_pos = start_pos
    landed_sandcorns += 1
  if current_sandcorn_pos[1] > min_y:
    # first sandcorn entered void
    print(current_sandcorn_pos)
    break


print("Amount of safely landed Sandcorns: ", landed_sandcorns)