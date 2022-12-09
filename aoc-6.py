# read in data

with open('aoc-6.txt') as t:
    datastreams = t.readlines()

datastreams = "".join([datastream.strip().split() for datastream in datastreams][0])

# find index for letter following a set of four letters with no repeats

count = 0

for index, letter in enumerate(datastreams):
    previous_four = datastreams[(index-4):index]
    count += 1
    if count > 4 and len(set(previous_four)) == len(previous_four):
        char_to_be_processed = index
        print(index)
        break

# find index for letter following a set of fourteen letters with no repeats

count = 0

for index, letter in enumerate(datastreams):
    previous_fourteen = datastreams[(index-14):index]
    count += 1
    if count > 14 and len(set(previous_fourteen)) == len(previous_fourteen):
        char_to_be_processed = index
        print(index)
        break
        
# refactor into one function for both parts

def finder(number_of_chars):

    count = 0

    for index, letter in enumerate(datastreams):
        previous_chars = datastreams[(index-number_of_chars):index]
        count += 1
        if count > number_of_chars and len(set(previous_chars)) == len(previous_chars):
            char_to_be_processed = index
            print(index)
            break

finder(4)
finder(14)
