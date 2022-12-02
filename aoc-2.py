# read in data

with open('aoc-2.txt') as t:
    matches = t.readlines()

matches = [match.strip().split() for match in matches]

# set up mappings

moves = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}

points = {"rock": 1, "paper": 2, "scissors": 3, "win": 6, "loss": 0, "draw": 3}

# map matches

matches = [[moves[i] for i in match] for match in matches]

#

def find_outcome(match):
    if match[0] == "rock":
        if match[1] == "rock":
            result = "draw"
        elif match[1] == "paper":
            result = "win"
        else:
            result = "loss"
    elif match[0] == "paper":
        if match[1] == "paper":
            result = "draw"
        elif match[1] == "scissors":
            result = "win"
        else:
            result = "loss"
    else:
        if match[1] == "scissors":
            result = "draw"
        elif match[1] == "rock":
            result = "win"
        else:
            result = "loss"

    match.append(result)

for match in matches:
    find_outcome(match)

# map to points

matches = [[points[i] for i in match] for match in matches]

# score my plays

my_scores = [match[1] + match[2] for match in matches]

# find my total score

print(sum(my_scores))
