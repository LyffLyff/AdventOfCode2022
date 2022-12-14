

fully_contained_counter : int = 0

f = open("input.txt", "r")
input = f.read().replace("\n", ",").split(",")


for i in range(0, len(input) - 1, 2):
  first_assorted : list = input[i].split("-")
  second_assorted : list = input[i  + 1].split("-")
  if (int(first_assorted[0]) >= int(second_assorted[0]) and int(first_assorted[1]) <= int(second_assorted[1])) or (int(first_assorted[0]) <= int(second_assorted[0]) and int(first_assorted[1]) >= int(second_assorted[1]) ):
    fully_contained_counter += 1


print("So many assorted times are overlapping completely with each other: ", fully_contained_counter)