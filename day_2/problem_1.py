f = open("input.txt", "r")
lines = f.readlines()
f.close()

directions = {'forward': 0, 'down': 0, 'up': 0}
for line in lines:
    direction = line.split(' ')[0]
    value = int(line.split(' ')[1])
    directions[direction] += value 
print(directions['forward'] * (directions['down'] - directions['up']))