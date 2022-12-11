# read in data

assignments = [assignment.strip() for assignment in open("aoc-4.txt")]

# find number of assignments fully containing the other pair, or any element of the other pair

contained_within = 0
any_overlap = 0

for assignment in assignments:
    assignment = assignment.replace(",", "-").split("-")
    first_section = [i for i in range(int(assignment[0]), int(assignment[1]) + 1)]
    second_section = [i for i in range(int(assignment[2]), int(assignment[3]) + 1)]
    if set(first_section).issubset(set(second_section)) or set(second_section).issubset(set(first_section)):
        contained_within += 1
    if len(set(first_section).intersection(set(second_section))) != 0:
        any_overlap += 1
    
print(contained_within)
print(any_overlap)
