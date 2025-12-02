import math

FILE_NAME = "input.txt"


# Given list of ranges, find sum of all the invalid product ids
# Invalid product ids:
# - only made of sequence of digits repeated twice
# - have leading zeroes
def sum_invalid_product_ids(line):
    sum = 0
    ranges = line.split(",")
    for r in ranges:
        # Get start/stop in range
        splits = r.split("-")
        # Convert to numbers
        start = int(splits[0])
        stop = int(splits[1])
        # Iterate over numbers in range, +1 for inclusive
        for i in range(start, stop + 1):
            # Skip single digits
            if i < 10:
                continue
            i_str = str(i)
            # Repeated twice can only happen in even length numbers
            if len(i_str) % 2 == 0:
                half = math.floor(len(i_str) / 2)
                # Check if first half matches last half
                if i_str[half:] == i_str[:half]:
                    sum += i
    return sum


# Invalid numbers are any repeated at least twice
def sum_invalid_product_ids_2(line):
    sum = 0
    ranges = line.split(",")
    for r in ranges:
        # Get start/stop in range
        splits = r.split("-")
        # Convert to numbers
        start = int(splits[0])
        stop = int(splits[1])
        # Iterate over numbers in range, +1 for inclusive
        for i in range(start, stop + 1):
            # Skip single digits
            if i < 10:
                continue
            i_str = str(i)
            # Window is size of substring/subnumber in number, i
            # Biggest window is half of the overall length, which will be 2 duplicates
            for window in range(1, math.floor(len(i_str) / 2) + 1):
                # Skip any window that doesn't fit evenly in number, i
                if len(i_str) % window != 0:
                    continue
                # Substring
                base = i_str[:window]
                # Determine amount of repetitions in number, i
                repetitions = math.floor(len(i_str) / window)
                # Check if repetitions of base equal number, i
                if base * repetitions == i_str:
                    sum += i
                    break
    return sum


# Part 1
# example_input: 1227775554
# input: 31000881061
with open(FILE_NAME, "r") as file:
    line = file.readline()
    print("Part 1:", sum_invalid_product_ids(line))

# Part 2
# example_input: 4174379265
# input: 46769308485
with open(FILE_NAME, "r") as file:
    line = file.readline()
    print("Part 2:", sum_invalid_product_ids_2(line))
