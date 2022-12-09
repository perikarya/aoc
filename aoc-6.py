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
