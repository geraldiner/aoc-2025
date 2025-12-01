import math

DIAL_START = 50
FILE_NAME = "input.txt"


# Count each stop at 0
def determine_password(lines):
    number_of_zeros = 0
    current = DIAL_START
    for line in lines:
        # get first character, L or R
        direction = line[0]
        # get number for rotations
        rotations = int(line[1:])
        # since full rotations are in units of 100, take the remainder
        rotations_short = rotations % 100
        # if L going backwards, otherwise go forwards
        if direction == "L":
            current -= rotations_short
        else:
            current += rotations_short

        # account for circle
        if current < 0:
            current += 100
        elif current > 99:
            current -= 100

        # increment zero count
        if current == 0:
            number_of_zeros += 1
    return number_of_zeros


# Counts any time the dial points at or passes 0
def determine_password_2(lines):
    number_of_zeros = 0
    current = DIAL_START
    for line in lines:
        # set a prev tracker for rounds that start at 0,
        # which should not be doubled-counted
        prev = current
        # get first character, L or R
        # get first character, L or R
        direction = line[0]
        # get number for rotations
        rotations = int(line[1:])
        # since full rotations are in units of 100, take the remainder
        rotations_short = rotations % 100
        # if rotations is greater than 100, count the number of times
        # the dial would pass 0
        if rotations >= 100:
            number_of_zeros += math.floor(rotations / 100)
        # if L going backwards, otherwise go forwards
        if direction == "L":
            current -= rotations_short
        else:
            current += rotations_short

        # account for circle
        # count for passing 0, but only if not already pointed at 0
        if current < 0 or current > 99:
            if prev != 0:
                number_of_zeros += 1
            if current < 0:
                current += 100
            elif current > 99:
                current -= 100
        elif current == 0:
            number_of_zeros += 1

    return number_of_zeros


# Part 1
with open(FILE_NAME, "r") as file:
    lines = file.readlines()
    print("Part 1: ", determine_password(lines))

# Part 2
with open(FILE_NAME, "r") as file:
    lines = file.readlines()
    print("Part 2: ", determine_password_2(lines))
