f = open("input.txt", "r")
numbers = f.readlines()[0].split(",")

numbers = list(map(int, numbers))

def calc_cost(steps):
    return (1 + steps) * steps // 2

min_fuel = float('inf')
for i in range(min(numbers), max(numbers)):
    fuels_used = 0
    for num in numbers: fuels_used += calc_cost(abs(num - i))
    min_fuel = min(min_fuel, fuels_used)

print(min_fuel)