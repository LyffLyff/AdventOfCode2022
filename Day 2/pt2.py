# pt2

f = open("input.txt", "r")
input = f.read().splitlines()

score : int = 0
opponent_hand : str = ""
your_hand : str = ""
your_finish : str = ""

result_scores : dict = {
    "Win" : 6,
    "Loss" : 0,
    "Draw" : 3
}

hands = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win"
}


def get_your_hand_score() -> str:
    match [your_finish, opponent_hand]:
        case ["Win", "Scissors"] | ["Draw", "Rock"] | ["Loss", "Paper"]:
            # everytime rock is the answer
            return 1
        case ["Win", "Rock"] | ["Draw", "Paper"] | ["Loss", "Scissors"]:
            # everytime paper has been used
            return 2
        case ["Win", "Paper"] | ["Draw", "Scissors"] | ["Loss", "Rock"]:
            # everytime scissor has been used
            return 3
        

for x in range(len(input)):
    for y in range(len(input[x])):
        match input[x][y]:
            case "A" | "B" | "C":
                opponent_hand = hands.get(input[x][y])
            case "X" | "Y" | "Z":
                your_finish = hands.get(input[x][y])
                score += result_scores.get(your_finish)
            case _:
                your_finish = ""
    
    if your_finish != "":
        score += get_your_hand_score()

print(score)