

LOWERCASE_OFFSET : int = 96
UPPERCASE_OFFSET : int = 38

common_items : list = []
priority_sum : int = 0

f = open("input.txt", "r")
input = f.read().splitlines()

compartment_content : list = [[],[]]

def get_priority(item : str) -> int:
  if item.isupper():
    return ord(item) - UPPERCASE_OFFSET
  else:
    return ord(item) - LOWERCASE_OFFSET

for rucksack_content in input:
  # getting each compartment of rucksack
  compartment_content[0] = rucksack_content[0:int(len(rucksack_content) / 2)]
  compartment_content[1] = rucksack_content[int(len(rucksack_content) / 2):len(rucksack_content)]

  # finding common items
  for comp1_item in compartment_content[0]:
    if comp1_item in compartment_content[1]:
      priority_sum += get_priority(comp1_item)
      break


print("Sum of Common Items between compartements is: " ,priority_sum)
