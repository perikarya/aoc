# read in data

with open('aoc-2.txt') as t:
    matches = t.readlines()

matches = [match.strip().split() for match in matches]

# set up mappings

moves = {"A": "rock", "B": "paper", "C": "scissors", "X": "loss", "Y": "draw", "Z": "win"}

points = {"rock": 1, "paper": 2, "scissors": 3, "win": 6, "loss": 0, "draw": 3}

# map matches

matches = [[moves[i] for i in match] for match in matches]

# for the second part, we are reversing the outcome finder to decide the move based on the outcome

def find_outcome(match):

    if match[0] == "rock":
        if match[1] == "draw":
            move = "rock"
        elif match[1] == "win":
            move = "paper"
        else:
            move = "scissors"
    elif match[0] == "paper":
        if match[1] == "draw":
            move = "paper"
        elif match[1] == "win":
            move = "scissors"
        else:
            move = "rock"
    else:
        if match[1] == "draw":
            move = "scissors"
        elif match[1] == "win":
            move = "rock"
        else:
            move = "paper"

    match.append(move)

for match in matches:
    find_outcome(match)

# map to points

matches = [[points[i] for i in match] for match in matches]

# score my plays

my_scores = [match[1] + match[2] for match in matches]

# find my total score

print(sum(my_scores))
