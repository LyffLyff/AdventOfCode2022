# part 1 of the second day of advent of code day optimized

# 1 -> Rock
# 2 -> Paper
# 3 -> Scissors
combinations = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

score : int = 0
opponent_hand : int = -1
your_hand : int = -1


def get_result(your_hand : int , opponent_hand : int) -> int:
  match your_hand - opponent_hand:
    case 1 | -2:
      #  you win
      return 6
    case 0:
      # draw
      return 3
  # if the opponents hand is greater in any margin they have won
  return 0

f = open("input.txt", "r")
input = f.read().splitlines()

for x in input:
  for y in range(len(x)):
    match x[y]:
        case "A" | "B" | "C":
            opponent_hand = combinations.get(x[y])
        case "X" | "Y" | "Z":
            your_hand = combinations.get(x[y])
            score += your_hand
            break
  score += get_result(your_hand, opponent_hand)

print("Your final score is: ", score)