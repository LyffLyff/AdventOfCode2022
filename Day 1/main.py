# https://adventofcode.com/2022/day/1




f = open("input.txt","r")
input = f.read().splitlines()


print(input)

max_cal : int = 0
current_cal : int = 0
current_elf_idx : int = 0
max_elf_idx : int = 0


for i in range(len(input)):
  if input[i] == "":
   
    if current_cal > max_cal:
      max_cal = current_cal
      max_elf_idx = current_elf_idx
   
    current_elf_idx += 1
    current_cal = 0
  else:
    print(input[i])
    current_cal += int(input[i])


print("Elf: ", str(current_elf_idx), "carries most with: ", str(max_cal), " Calories")