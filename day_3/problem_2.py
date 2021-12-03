f = open("input.txt", "r")
lines = f.readlines()
f.close()

def helper(lines, digits, frequency):
    for i in range(digits):
        lines_with_1 = []
        lines_with_0 = []
        for line in lines:
            if line[i] == '1': lines_with_1.append(line)
            else: lines_with_0.append(line)
        if len(lines_with_1) + len(lines_with_0) == 1:
            return lines_with_1[0] if len(lines_with_1) == 1 else lines_with_0[0]
        if frequency == 'max':
            lines = lines_with_1 if len(lines_with_1) >= len(lines_with_0) else lines_with_0
        elif frequency == 'min':
            lines = lines_with_1 if len(lines_with_1) < len(lines_with_0) else lines_with_0
    return lines[0]

digits = len(lines[0]) - 1
print(int(helper(lines, digits, 'max'), 2) * int(helper(lines, digits, 'min'), 2))