# read in data

treelines = [treeline.split() for treeline in open("aoc-8.txt")]

treeline_nums = []

for row in treelines:
    for items in row:
        row = [int(items) for items in str(items)]
        treeline_nums.append(row)

# array

import numpy as np

tree_grid = np.array(treeline_nums)

length = tree_grid.shape[0]
width = tree_grid.shape[1]

# count edge trees

visible_trees = (length * 2) + (width * 2) - 4

# check if tree is visible

for row in range(1, length - 1):
    for col in range(1, width - 1):
        tree = tree_grid[row][col]
        if tree > np.amax(tree_grid[row, 0:col]):
            visible_trees += 1
        elif tree > np.amax(tree_grid[row, (col + 1):width]):
            visible_trees += 1
        elif tree > np.amax(tree_grid[0:row, col]):
            visible_trees += 1
        elif tree > np.amax(tree_grid[(row + 1):width, col]):
            visible_trees +=1

print(visible_trees)

# scenic score

scenic_scores = np.zeros(tree_grid.shape)

for row in range(1, length - 1):
    for col in range(1, width - 1):
        tree = tree_grid[row][col]
        left = tree_grid[row, 0:col]
        right = tree_grid[row, (col + 1):width]
        up = tree_grid[0:row, col]
        down = tree_grid[(row + 1):length, col]
        sides = [np.flip(left), right, np.flip(up), down]
        scenic_list = [np.where(side >= tree)[0][0] + 1 if np.any(side >= tree) else side.size for side in sides]
        scenic = np.prod(np.array(scenic_list))
        scenic_scores[row, col] = scenic

print(np.max(scenic_scores))