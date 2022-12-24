# https://adventofcode.com/2022/day/13

import ast
from itertools import zip_longest

f = open("input.txt", "r")
input = f.read().splitlines()
f.close()


def compare(packet_1 : list, packet_2 : list):
  for p1, p2, in zip_longest(packet_1, packet_2, fillvalue=None):
    
    # check if ran out of indices
    if p1 == None:
      # left ran out of indices -> RIGHT ORDER
      return True
    if p2 == None:
      # right ran out of indices -> WRONG ORDER
      return False
    
    if isinstance(p1, int) and isinstance(p2, int):
      if p1 > p2:
        return False
      elif p1 < p2:
        return True
    else:
      # converting inner int to lists if both are not integers
      if isinstance(p1, int):
        p1 = [p1]
      if isinstance(p2, int):
        p2 = [p2]
      
      # comparing inner packets
      inner_compare = compare(p1, p2)
      if inner_compare != None:
        return inner_compare
      
packets : list = []
correct_packets_indices : list = []

# convert input to packets
for i in input:
  if i != '':
    packets.append(ast.literal_eval(i))


# compare packets
for i in range(0, len(packets), 2):
  # go through each duo of packets
  print("INDEX: ",i//2 + 1)
  if compare(packets[i], packets[i + 1]):
    correct_packets_indices.append((i // 2) + 1)


print("CORRECT INDICES: ", correct_packets_indices)
print("THE SUM OF THE INDICES OF PACKETRS WHICH WERE CORRECT IS: ", sum(correct_packets_indices))
