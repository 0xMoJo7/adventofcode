import math


def part_one():
    fuel_needed = 0
    with open('day1_data.txt') as f:
        for planet_mass in f.readlines():
            fuel_needed += math.floor(int(planet_mass.rstrip())/3) - 2
    return fuel_needed
