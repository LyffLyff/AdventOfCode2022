# https://adventofcode.com/2022/day/11
from re import findall
from pprint import pprint

input = open("input.txt", "r").read().splitlines()

monkeys : dict = {}
MAX_ROUNDS : int = 20
current_round : int = 1

# init each monkey
for i in range(0, len(input), 7):
  monkeys[int(findall(r'\d+', input[i])[0])] = {
    "items" : [int(i) for i in findall(r'\d+', input[i + 1])],
    "anxiety_increase" : findall(r'\d+', input[i + 2]),
    "anxiety_increase_operator" : input[i + 2][input[i + 2].find("old ") + 4],
    "test" : int(findall(r'\d+', input[i + 3])[0]),
    "test_true" : int(findall(r'\d+', input[i + 4])[0]),
    "test_false" : int(findall(r'\d+', input[i + 5])[0]),
    "inspections" : 0
  }

pprint(monkeys)

# rounds
for current_round in range(0, MAX_ROUNDS):
  #print("NEW ROUND: ", current_round)
  #pprint(monkeys)
  for i in range(len(monkeys)):
    items_dst : list = [] #[[src, dst]]
    # get item source and destination
    for j in range(len(monkeys[i]["items"])):
      # incrementing inspections
      monkeys[i]["inspections"] += 1
      # calculate anxiety after inspection
      item_src : int = monkeys[i]["items"][j]
      if len(monkeys[i]["anxiety_increase"]) > 0:
        match monkeys[i]["anxiety_increase_operator"]:
          case '+':
            item_src += int(monkeys[i]["anxiety_increase"][0])
          case '*':
            item_src *= int(monkeys[i]["anxiety_increase"][0])
          case _:
            print("SOMETHING WENT WRONG MY GUY!")
      else:
        item_src = item_src ** 2
      item_src //= 3
      
      # throwing item
      if item_src % monkeys[i]["test"] == 0:
        items_dst.append([item_src, monkeys[i]["test_true"]])
      else:
        items_dst.append([item_src, monkeys[i]["test_false"]])
    
    # add items to corresponding monkey
    for k in range(len(items_dst)):
      monkeys[items_dst[k][1]]["items"].append(items_dst[k][0])
    
    # free current monkeys item list
    monkeys[i]["items"].clear()

# get monkey business level -> multiplying the top 2 inspectors
inspections : list = []
for i in range(len(monkeys)):
  inspections.append(monkeys.get(i)["inspections"])

inspections = sorted(inspections, reverse=True)

print("Monkey Inspections: ", inspections)
print("MONKEY BUSINESS LEVEL AFTER 20 ROUNDS: ", inspections[0] * inspections[1])
