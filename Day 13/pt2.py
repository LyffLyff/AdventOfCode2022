# https://adventofcode.com/2022/day/13

import ast
from itertools import zip_longest
from pprint import pprint

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
divider_packets : list = [[[2]],[[6]]]
sorted_packets : list = []

# convert input to packets
for i in input:
  if i != '':
    packets.append(ast.literal_eval(i))


# appeding distress signals to packets to be sorted aswell
packets.extend(divider_packets)

# compare packets
for i in range(len(packets)):
  for j in range(len(sorted_packets)):
    print("J: ",sorted_packets[j])
    print("I: ",packets[i])
    if compare(packets[i], sorted_packets[j]):
      print("INSERT AT: ", i)
      sorted_packets.insert(j, packets[i])
      print(sorted_packets)
      break
  else:
    print("APPEND AT END")
    sorted_packets.append(packets[i])


pprint(sorted_packets)
print("DECODER KEY: ", (sorted_packets.index(divider_packets[0]) + 1) * (sorted_packets.index(divider_packets[1]) + 1))