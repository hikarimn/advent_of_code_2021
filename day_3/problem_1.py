f = open("input.txt", "r")
lines = f.readlines()
f.close()

digits = len(lines[0]) - 1
freq_counter = [0 for _ in range(digits)]

for line in lines:
    for i in range(digits):
        if line[i] == '1': freq_counter[i] += 1
        else: freq_counter[i] -= 1

gamma = int(''.join(list(map(lambda x: '1' if x < 0 else '0', freq_counter))), 2)
epsilon = int(''.join(list(map(lambda x: '0' if x < 0 else '1', freq_counter))), 2)

print(gamma * epsilon)