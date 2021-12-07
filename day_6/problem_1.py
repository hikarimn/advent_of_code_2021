f = open("input.txt", "r")
timers = f.readlines()[0].split(",")

timers = list(map(int, timers))

# naive solution...

for i in range(256):
    new_timers = []
    zero_counter = 0
    print(timers)

    for index, timer in enumerate(timers):
        if timer == 0:
            new_timers.append(6)
            zero_counter += 1
        else:
            new_timers.append(timer - 1)
    for _ in range(zero_counter): new_timers.append(8)
    
    timers = new_timers
    print(i)

print(len(timers))