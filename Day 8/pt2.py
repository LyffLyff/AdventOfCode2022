# https://adventofcode.com/2022/day/8

visible_from_outside : int = 0
most_scenic_tree_score : int = 0

input = open("input.txt", "r").read().splitlines()

def get_top_score(x : int, y : int, height : int) -> int:
  score : int = 0
  y_offset : int = 0-1
  while True:
    new_y = y + y_offset
    if input[new_y][x] >= height:
      score += 1
      break
    else:
      score += 1
    if new_y == 0:
      break
    y_offset -= 1
  return score


def get_bottom_score(x : int, y : int, height : int) -> int:
  score : int = 0
  y_offset : int = +1
  while True:
    new_y = y + y_offset
    if input[new_y][x] >= height:
      score += 1
      break
    else:
      score += 1
    if new_y == len(input) - 1:
      break
    y_offset += 1
  return score

def get_right_score(x : int, y : int, height : int) -> int:
  score : int = 0
  x_offset : int = +1
  while True:
    new_x = x + x_offset
    if input[y][new_x] >= height:
      score += 1
      break
    else:
      score += 1
    if new_x == len(input[x]) - 1:
      break
    x_offset += 1
  return score

def get_left_score(x : int, y : int, height : int) -> int:
  score : int = 0
  x_offset : int = -1
  while True:
    new_x = x + x_offset
    if input[y][new_x] >= height:
      score += 1
      break
    else:
      score += 1
    if new_x == 0:
      break
    x_offset -= 1
  return score

def get_scenery_score(x : int, y : int, height : int) -> int:
   # checking if one of the trees at the edge
  if y == 0 or x == 0 or x == len(input[x]) - 1 or y == len(input) - 1:
    return 0
  
  # getting score
  return get_top_score(x, y, height) * get_bottom_score(x, y, height) * get_left_score(x, y, height) * get_right_score(x, y, height)

print(input)

# left to right
for y in range(len(input)):
  visible = True
  for x in range(len(input[y])):
    new_score = get_scenery_score(x, y, input[y][x])
    if new_score > most_scenic_tree_score:
      most_scenic_tree_score = new_score


print("THE MOST SCENIC TREE HAS A SCORE OF: ", most_scenic_tree_score)
    
    