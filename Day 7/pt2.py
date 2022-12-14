# https://adventofcode.com/2022/day/7

import re
import json

current_dir_name : str = ""
dir_tree : dict = {}
dir_size : int = 0
sum_of_directories : int = 0
current_path : list = []
every_directory : list = []
occupied_space : int = -1
smallest_dir_to_delete : int = 0
TOTAL_DISK_SPACE : int = 70000000
MIN_REQUIRED_SPACE : int = 30000000

def add_file_to_directory(directory_path : list, key : str, value) -> None:
  print("PATH: ", directory_path)
  print("XX:" ,get_inner_directory(directory_path))
  get_inner_directory(directory_path)[key] = value


def get_inner_directory(directory_path : list) -> dict:
  temp_dict : dict = dir_tree
  for i in range(len(directory_path)):
    if i == 0:
      temp_dict = dir_tree.get(directory_path[i])
    else:
      temp_dict = temp_dict.get(directory_path[i])
  return temp_dict


def get_dir_size(dir : dict) -> int:
  global dir_below_threshold
  dir_size : int = 0
  for i in dir:
    if isinstance(dir[i], int):
      dir_size += dir[i]
    elif isinstance(dir[i], dict):
      dir_size += get_dir_size(dir[i])
  every_directory.append(dir_size)
  return dir_size


input = open("input.txt", "r").read().split("\n")

# creating directory tree
for i in range(len(input)):
  if "$" in input[i]:
    print("Command: ", input[i])
    if input[i].startswith("$ cd "):
      # the directory being changed to 
      print("DIRECTORY: ", input[i][5:])
      match input[i][5:]:
        case "..":
          current_path.pop(-1)
        case "/":
          current_path = []
        case _:
          print("SWITHCHCHCHH: ", input[i][5:])
          current_path.append(input[i][5:])
    elif input[i].startswith("$ ls"):
      pass
  elif input[i] != "":
    print("Output: ", input[i])
    if "dir" in input[i]:
      print("!DIR: ", input[i][4:])
      dir_name = input[i][4:]
      add_file_to_directory(current_path, dir_name, {})
    elif input[i][0].isalnum():
      number_end : int = input[i].find(" ")
      print("FILE: ", input[i])
      add_file_to_directory(current_path, input[i][number_end + 1:], int(input[i][0:number_end]))

print(json.dumps(dir_tree, indent=4))
occupied_space = get_dir_size(dir_tree)
print("SUM OF WHOLE FILE TREE: " , occupied_space)
if TOTAL_DISK_SPACE - occupied_space < MIN_REQUIRED_SPACE:
  print("SORTED LIST OF EVERY DIRECTORY IN THE FILESYSTEM: " ,sorted(every_directory))
  every_directory = sorted(every_directory)
  min_space_required : int = MIN_REQUIRED_SPACE - (TOTAL_DISK_SPACE - occupied_space)
  print("SPACE REQUIRED: ", min_space_required)
  for i in every_directory:
    print(i)
    if i >= min_space_required:
      smallest_dir_to_delete = i
      break

print("SMALLEST DIR THAT ALLOWS THE ELVES TO INSTALL UPDATE: ", smallest_dir_to_delete)

