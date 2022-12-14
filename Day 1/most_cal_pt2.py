# https://adventofcode.com/2022/day/1


f = open("input.txt","r")
input = f.read().splitlines()


print(input)

max_cals : list = [0,0,0]
current_cal : int = 0
current_elf_idx : int = 0
max_elfs_idx : list = [0,0,0]


for i in range(len(input)):
  if input[i] == "":
      for j in range(len(max_cals)):
        if current_cal > max_cals[j]:
          max_cals.insert(j, current_cal)
          max_cals.pop(3)
          max_elfs_idx.insert(j, current_elf_idx)
          max_elfs_idx.pop(3)
          break;
      
      current_elf_idx += 1
      current_cal = 0   
  else:
    current_cal += int(input[i])


print("Elfs:", str(current_elf_idx), "carrying most with: ", max_cals, " Calories")

print("Combined Calories:", sum(max_cals))