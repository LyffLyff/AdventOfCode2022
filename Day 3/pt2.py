# https://adventofcode.com/2022/day/3

LOWERCASE_OFFSET : int = 96
UPPERCASE_OFFSET : int = 38

priority_sum : int = 0

f = open("input.txt", "r")
input = f.read().splitlines()

def get_priority(item : str) -> int:
  if item.isupper():
    return ord(item) - UPPERCASE_OFFSET
  else:
    return ord(item) - LOWERCASE_OFFSET


for x in range(0, len(input), 3):
  # looping through characters of first group
  # and checking if each item is within the other group members rucksack
  for item in input[x]:
    if (item in input[x + 1]) and (item in input[x + 2]):
      priority_sum += get_priority(item)
      break


print("Sum of a groups unique identifier are: " ,priority_sum)
