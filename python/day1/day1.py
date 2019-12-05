import math


def calc_fuel(planet_mass):
    return math.floor(planet_mass/3) - 2


def part_one():
    planets = [int(line.rstrip()) for line in open('day1_data.txt').readlines()]
    fuel_needed = 0
    for planet_mass in planets:
        fuel_needed += calc_fuel(planet_mass)
    return fuel_needed


def part_two():
    planets = [int(line.rstrip()) for line in open('day1_data.txt').readlines()]
    fuel_needed = 0
    for mass in planets:
        fuel_req = mass  # init fuel_req > 0
        while fuel_req > 0:
            fuel_req = calc_fuel(fuel_req)
            fuel_needed += fuel_req
    return fuel_needed
