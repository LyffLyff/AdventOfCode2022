# https://adventofcode.com/2022/day/8

visible_from_outside : int = 0

input = open("input.txt", "r").read().splitlines()

def check_above(x : int, y : int, height : int) -> bool:
  y_offset : int = -1
  while True:
    new_y = y + y_offset
    if input[new_y][x] >= height:
      return False
    if new_y == 0:
      return True
    y_offset -= 1

def check_below(x : int, y : int, height : int) -> bool:
  y_offset : int = 1
  while True:
    new_y = y + y_offset
    if input[new_y][x] >= height:
      return False
    if new_y == len(input) - 1:
      return True
    y_offset += 1

def check_right(x : int, y : int, height : int) -> bool:
  x_offset : int = 1
  while True:
    new_x = x + x_offset
    if input[y][new_x] >= height:
      return False
    if new_x == len(input[x]) - 1:
      return True
    x_offset += 1

def check_left(x : int, y : int, height : int) -> bool:
  x_offset : int = -1
  while True:
    new_x = x + x_offset
    if input[y][new_x] >= height:
      return False
    if new_x == 0:
      return True
    x_offset -= 1

def check_if_visible(x : int, y : int, height : int) -> bool:
  # checking if one of the trees at the edge
  if y == 0 or x == 0 or x == len(input[x]) - 1 or y == len(input) - 1:
    return True
  
  # checking the middle ones
  if check_above(x, y, height) or check_below(x, y, height) or check_left(x, y, height) or check_right(x, y, height):
    return True
  return False

print(input)

# left to right
for y in range(len(input)):
  visible = True
  for x in range(len(input[y])):
    if check_if_visible(x, y, input[y][x]):
      visible_from_outside += 1


print("AMOUNT OF TREES VISIBLE FROM OUTSIDE: ", visible_from_outside)
    
    