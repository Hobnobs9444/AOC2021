# Advent of Code Day 6 puzzle solution

# Import libraries
from collections import defaultdict

# Import file
my_file = open("day6_input.txt","r")
population = my_file.read().split(',')
population = [int(i) for i in population]

# Define function
def how_many_lanternfish_on_day(day):
    fishmap = defaultdict(int)

    for fish in population:
        # read input and map number of fish at each age into dictionary
        if fish not in fishmap:
            fishmap[fish] = 0
        fishmap[fish] += 1

    for day in range(day):
        # pass days aging and spawning new fish
        updatedfishmap = defaultdict(int)

        for fish, count in fishmap.items():
            if fish == 0:
                updatedfishmap[6] += count # reset age counter for these fish
                updatedfishmap[8] += count # spawn new fish 
            else:
                updatedfishmap[fish-1] += count # reduce age counter by 1
        
        fishmap = updatedfishmap

    print(f'On day {day+1} there will be {sum(fishmap.values())} Lanternfish')

# call function on required number of days
how_many_lanternfish_on_day(80)
how_many_lanternfish_on_day(256)