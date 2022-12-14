# 



f = open("input.txt", "r")
input = f.read().splitlines()

score : int = 0
opponent_hand : str = ""
your_hand : str = ""
hand_scores : dict = {
    "Scissors": 3,
    "Rock" : 1,
    "Paper" : 2
}
hands = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}


def get_received_score() -> int:

    if opponent_hand == your_hand:
        return 3
    

    match [opponent_hand, your_hand]:
        case ["Rock", "Paper"] | ["Paper", "Scissors"] | ["Scissors", "Rock"]:
        
            return 6
    return 0

for x in range(len(input)):
    for y in range(len(input[x])):
        match input[x][y]:
            case "A" | "B" | "C":
                opponent_hand = hands.get(input[x][y])
            case "X" | "Y" | "Z":
                your_hand = hands.get(input[x][y])
                score += hand_scores.get(your_hand)
            case _:
                your_hand = ""
    
    if your_hand != "":
        score += get_received_score()

print(score)