# https://adventofcode.com/2022/day/6

MARKER_LENGTH : int = 4
MESSAGE_START_LENGTH : int = 14

current_idx : int = 0
chars_to_marker : int = 0
chars_to_message : int = 0
message_found : bool = False
marker_found : bool = False

input = open("input.txt", "r").read()

while not message_found:
  temp = []
  if not marker_found:
    # searching for start marker
    for i in range(MARKER_LENGTH):
      if input[current_idx + i] in temp:
        break
      temp.append(input[current_idx + i])
    else:
      marker_found = True
      chars_to_marker = current_idx + MARKER_LENGTH
  else:
    # searching for message
    for i in range(MESSAGE_START_LENGTH):
      if input[current_idx + i] in temp:
        break
      temp.append(input[current_idx + i])
    else:
      message_found = True
      chars_to_message = current_idx + MESSAGE_START_LENGTH
  current_idx += 1

print("END OF FIRST MESSAGE MARKER: ", chars_to_message)