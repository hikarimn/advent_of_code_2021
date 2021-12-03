f = open("input.txt", "r")
lines = f.readlines()
f.close()

aim = 0
horizontal = 0
depth = 0
for line in lines:
    direction = line.split(' ')[0]
    value = int(line.split(' ')[1])
    if direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    elif direction == 'forward':
        horizontal += value
        depth += aim * value
print(horizontal * depth)