# https://adventofcode.com/2022/day/5

import re


stacks_grid : list = []
containers : dict = {}
commands : list = []

def move_container_to(src : int, dst : int, amount : int) -> dict:
  print("B: ",containers)
  for i in range(amount):
    containers[dst].append(containers[src].pop())
  print("A: ",containers)


input = open("input.txt", "r").read().split("move")

stacks : list = input[0].split("\n")
stacks.pop()
stacks.pop()
stacks.pop()


# init container
for i in range(9):
  containers[i + 1] = []

# extracts columns
for j in range(len(stacks) - 1, -1, -1):
  for i in range(1, len(stacks[j]), 4):
    if stacks[j][i] != ' ':
      containers[int(i / 4) + 1].append(stacks[j][i])

# extract commands
for i in range(1, len(input)):
  # extracting all numbers from the line
  commands.append(re.findall(r'\d+', input[i]))

cmd_src : int = 0
cmd_dst : int = 0
amount : int = 0
src_container : str = ""

for i in commands:
  # get commands values
  amount = int(i[0])
  cmd_src = int(i[1]) 
  cmd_dst = int(i[2])
  print("CMD: ", i)
  move_container_to(cmd_src, cmd_dst, amount)


print(containers)

for i in containers.keys():
  print(containers.get(i).pop(-1), end="")
