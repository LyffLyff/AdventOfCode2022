# https://adventofcode.com/2022/day/11
from re import findall
from pprint import pprint
from numpy import uint8

f = open("input.txt", "r")
input = f.read().splitlines()
f.close()

monkeys : dict = {}
MAX_ROUNDS : int = 10_000
supermodulo : int = 1

# init each monkey
for i in range(0, len(input), 7):
  temp : list = findall(r'\d+', input[i + 2])
  anxiety_increase : uint8 = -1
  if len(temp) > 0:
    anxiety_increase = int(temp[0])
  monkeys[int(findall(r'\d+', input[i])[0])] = {
    "items" : [int(i) for i in findall(r'\d+', input[i + 1])],
    "anxiety_increase" : anxiety_increase,
    "anxiety_increase_operator" : input[i + 2][input[i + 2].find("old ") + 4],
    "test" : int(findall(r'\d+', input[i + 3])[0]),
    "true" : uint8(findall(r'\d+', input[i + 4])[0]),
    "false" : uint8(findall(r'\d+', input[i + 5])[0]),
    "inspections" : 0
  }

# calc supermodulo
# if the numbers do not get shortened they will be soooo large that it will take literal years for the 10k rounds to have finished
# supermodulo = product of every divisor the monkey use to decide where to throw the item
for x in range(len(monkeys)):
  supermodulo *= monkeys[x]["test"]

# rounds
for current_round in range(0, MAX_ROUNDS):
  print("CURRENT ROUND: ", current_round)
  for i in range(len(monkeys)):
    items_dst : list = [] #[[src, dst]]
    # get item source and destination
    # adding inspections
    monkeys[i]["inspections"] += len(monkeys[i]["items"])
    for j in range(len(monkeys[i]["items"])):
      # calculate anxiety after inspection
      item_src : uint8 = monkeys[i]["items"][j]
      if monkeys[i]["anxiety_increase"] != -1:
        match monkeys[i]["anxiety_increase_operator"]:
          case '+':
            item_src += monkeys[i]["anxiety_increase"]
          case '*':
            item_src *= monkeys[i]["anxiety_increase"]
          case _:
            print("SOMETHING WENT WRONG MY GUY!")
      else:
        item_src **= 2
      # throwing item

      if item_src % monkeys[i]["test"] == 0:
        item_src %= supermodulo
        monkeys[monkeys[i]["true"]]["items"].append(item_src)
      else:
        monkeys[monkeys[i]["false"]]["items"].append(item_src)
    
    # free current monkeys item list
    monkeys[i]["items"].clear()

# get monkey business level -> multiplying the top 2 inspectors
inspections : list = []
for i in range(len(monkeys)):
  inspections.append(monkeys.get(i)["inspections"])

inspections = sorted(inspections, reverse=True)

print("Monkey Inspections: ", inspections)
print("MONKEY BUSINESS LEVEL AFTER 10k ROUNDS: ", inspections[0] * inspections[1])
