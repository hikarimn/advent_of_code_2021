f = open("input.txt", "r")
lines = list(f.readlines())
f.close()
counter = -1
prev = 0

for i in range(0, len(lines) - 2):
    sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if sum > prev: counter += 1
    prev = sum
print(counter)