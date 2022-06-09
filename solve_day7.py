# Advent of code day 7 solution

def fuel_cost(locations, target):
    # Calculate fuel cost to move all crabs at starting 'locations' to 'target'
    total = 0
    for location in locations:
        total  += abs(location - target)
    return total

def part2_fuel_cost(locations, target):
    # Calculate fuel cost using Guass consecutive numbers eq
    total = 0
    for location in locations:
        n = abs(location - target)
        total += (n/2)*(1+n)
    return total


def test_range(locations):
    # Brute force solution to apply fuel_cost() to range of starting locations and return lowest fuel cost
    current_best = max(locations)**2
    for i in range(min(locations), max(locations)+1):
        cost = fuel_cost(locations, i)
        
        if cost < current_best:
            current_best = cost

    print(f'Part 1 Minimum fuel required is {current_best}')


def test_range_tenary(locations):
    # Tenary search algorithm to identify minimum fuel cost - used for part 2
    left = min(locations)
    right = max(locations)

    while abs(right-left) >= 3:
        left_third = round(left + (right - left) / 3)
        right_third = round(right - (right - left) / 3)

        if part2_fuel_cost(locations, left_third) > part2_fuel_cost(locations, right_third):
            left = left_third
        else:
            right = right_third

    best_location = (left + right) / 2

    print(f'Part 2 Best location is: {best_location}')
    print(f'Part 2 Fuel cost for this location is {part2_fuel_cost(locations, best_location)}')


def main():
    input = open('day7_input.txt').read().split(',')
    input = list(map(int, input))
    test_range(input)
    test_range_tenary(input)
   

if __name__ == '__main__':
    main()

