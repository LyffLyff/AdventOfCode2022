

overlap_counter : int = 0

f = open("input.txt", "r")
input = f.read().replace("\n", ",").split(",")


for i in range(0, len(input) - 1, 2):
  first_assorted : list = input[i].split("-")
  second_assorted : list = input[i  + 1].split("-")
  for j in range(2):
    if (int(second_assorted[j]) in range(int(first_assorted[0]), int(first_assorted[1]) + 1)) or (int(first_assorted[j]) in range(int(second_assorted[0]), int(second_assorted[1]) + 1)):
      overlap_counter += 1
      break


print("So many assorted times are overlapping with each other: ", overlap_counter)