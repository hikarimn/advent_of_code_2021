f = open("input.txt", "r")
numbers = f.readlines()[0].split(",")

numbers = list(map(int, numbers))

# naive solution...
min_fuel = sum(numbers)
for i in range(min(numbers), max(numbers)):
    fuels_used = 0
    for num in numbers: fuels_used += abs(num - i)
    min_fuel = min(min_fuel, fuels_used)

print(min_fuel)