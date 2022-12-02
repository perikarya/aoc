# read in data

with open('aoc-1.txt') as t:
    lines = t.readlines()

lines = [line.strip() for line in lines]

# set up lists of snacks carried by each elf

snacks = [[]]

for calories in lines:
    if calories != "":
        snacks[-1].append(int(calories))
    else:
        snacks.append([])

# set up dicts matching snack sets to each elf id

elves = {}

for elf, snack_set in enumerate(snacks):
    elves[elf] = snack_set

# calculate total calories carried by each elf

totals = {}

for elf_id, snack_set in elves.items():
    totals[elf_id] = sum(snack_set)

# find elf carrying most calories, and number of calories carried by that elf

top_elf = max(totals.items(), key = lambda x: x[1])
print(top_elf)

# find top three elves carrying the most calories,  number of calories carried by those elves

top_three_elves = sorted(totals.items(), key = lambda x: x[1], reverse = True)[:3]
sum_of_top_three = top_three_elves[0][1] + top_three_elves[1][1] + top_three_elves[2][1]
print(sum_of_top_three)