# https://adventofcode.com/2022/day/6


current_idx : int = 0
chars_to_marker : int = 0
marker_found : bool = False

input = open("input.txt", "r").read()

while not marker_found:
  if not marker_found:
    # searching for start marker
    temp = []
    for i in range(4):
      if input[current_idx + i] in temp:
        break
      temp.append(input[current_idx + i])
    else:
      marker_found = True
      chars_to_marker = current_idx + 4
  else:
    # searching for message
    print()
  current_idx += 1

print(chars_to_marker)
print("Marker: ", *temp, sep="")