# read in data

with open('aoc-3.txt') as t:
    rucksacks = t.readlines()

rucksacks = [rucksack.strip() for rucksack in rucksacks]

# divide into compartments

first_compartment = [rucksack[0:int((len(rucksack) / 2))] for rucksack in rucksacks]
second_compartment = [rucksack[int((len(rucksack) / 2)):] for rucksack in rucksacks]

# set up priorities

priorities = {}

letters = list(map(chr, range(97, 123)))
letters.extend(letter.upper() for letter in list(map(chr, range(97, 123))))

for priority, letter in enumerate(letters):
    priorities[letter] = priority + 1

# find items in both

items_in_both = []

for position, items in enumerate(first_compartment):
    item_in_both = ''.join(
        set(items).intersection(second_compartment[position]))
    items_in_both.append(item_in_both)

items_in_both = [priorities[i] for i in items_in_both]

sum_of_priorities = sum(items_in_both)
print(sum_of_priorities)
