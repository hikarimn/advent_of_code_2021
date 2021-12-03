f = open("input.txt", "r")

counter = -1
prev = 0
for line in f.readlines():
    if int(line) > prev: counter += 1
    prev = int(line)
f.close()
print(counter)