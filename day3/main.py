FILE_NAME = "example_input.txt"


# Find the max 2-digit number that can be created from the digits in the line
# ex: 818181911112111 => 92
def sum_max_jolts(lines):
    # Start sum
    sum = 0
    # Iterate over lines in input
    for line in lines:
        # Convert each digit to a number in a list
        digits = [int(d) for d in list(line)]
        # Find the first digit by finding the max excluding the last
        first_max = max(digits[: len(digits) - 1])
        # Get the index of the first digit
        first_max_index = digits.index(first_max)
        # Get a list of the remaining digits starting from the next digit from the max
        digits_trunc = digits[first_max_index + 1 :]
        # Find the max in the list of remaining digits
        second_max = max(digits_trunc)
        # Add the 2-digit number to the sum
        sum += int("".join([str(first_max), str(second_max)]))
    return sum


def sum_max_jolts_2(lines):
    sum = 0
    max_length = 12

    for line in lines:
        digits = [int(d) for d in list(line)]
        # Keep track of max jolt digits
        max_jolt = []
        window_end = len(digits) - (max_length - 1 - len(max_jolt))
        # Off by one fixer?
        start = -1

        # While there are remaining spaces for max jolt
        while len(max_jolt) < max_length:
            winner = max(digits[start + 1 : window_end])
            start = digits.index(winner, start + 1, window_end)
            window_end = len(digits) - (max_length - 2 - len(max_jolt))
            max_jolt.append(str(winner))
        sum += int("".join(max_jolt))
    return sum


# Part 1
# example_input: 357
# input: 16973
with open(FILE_NAME, "r") as file:
    lines = file.readlines()
    print("Part 1:", sum_max_jolts([l.strip() for l in lines]))

# Part 2
# example_input: 3121910778619
# input: 168027167146027
with open(FILE_NAME, "r") as file:
    lines = file.readlines()
    print("Part 2:", sum_max_jolts_2([l.strip() for l in lines]))
