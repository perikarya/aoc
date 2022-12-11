# read in data

assignments = [assignment.strip() for assignment in open("aoc-4.txt")]

# find number of assignments fully containing the other in the pair

count = 0

for assignment in assignments:
    assignment = assignment.replace(",", "-").split("-")
    first_section = [i for i in range(int(assignment[0]), int(assignment[1]) + 1)]
    second_section = [i for i in range(int(assignment[2]), int(assignment[3]) + 1)]
    if set(first_section).issubset(set(second_section)) or set(second_section).issubset(set(first_section)):
        count += 1
    
print(count)
