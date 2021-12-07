import re

def pretty_print(board):
    print('\n'.join('{}' for _ in range(len(board))).format(*board))
    print()

f = open("input.txt", "r")
lines = f.readlines()
f.close()

# first loop gets rid of the points that we do not consider
# and find the max of X and Y value
x_max, y_max = 0, 0
lines_to_consider = []

for line in lines:
    numbers = re.split('[^a-zA-Z0-9]+', line) 
    x1, y1, x2, y2 = int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])

    if x1 != x2 and y1 != y2: continue
    lines_to_consider.append(line)
    x_max, y_max = max(x_max, max(x1, x2)), max(y_max, max(y1, y2))

# second loop draws the matrix with a size of x_max and y_max
#  https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
matrix = [ [0] * (y_max + 1) for n in range(x_max + 1) ]

for line in lines_to_consider:
    numbers = re.split('[^a-zA-Z0-9]+', line) 
    x1, y1, x2, y2 = int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])

    if x1 == x2:
        starting_y = y1 if y1 < y2 else y2
        ending_y = y2 if y1 < y2 else y1
        for y in range(starting_y, ending_y + 1): matrix[y][x1] += 1 
    elif y1 == y2:
        starting_x = x1 if x1 < x2 else x2
        ending_x = x2 if x1 < x2 else x1
        for x in range(starting_x, ending_x + 1): matrix[y1][x] += 1

# we go over each number in the matrix and count how many points 2+ lines overlap
counter = 0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] >= 2: counter += 1
print(counter) 