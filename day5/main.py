FILE_NAME = "input.txt"

def count_fresh(lines):
    # Tracker for 
    count = 0
    ranges = []
    for line in lines:
        if len(line):
            if "-" in line:
                splits = line.split("-")
                ranges.append([int(splits[0]), int(splits[1])])
            else:
                num = int(line)
                for start, end in ranges:
                    if (num >= start and num <= end):
                        count += 1
                        break
    return count


def count_fresh_2(lines):
    count = 0
    ranges = []
    for line in lines:
        if len(line):
            if "-" in line:
                splits = line.split("-")
                ranges.append([int(splits[0]), int(splits[1])])
    ranges.sort(key = lambda i: i[0])
    merged_ranges = [ranges[0]]
    for start, end in ranges[1:]:
        lastEnd = merged_ranges[-1][1]
        if (start <= lastEnd):
            merged_ranges[-1][1] = max(end, lastEnd)
        else:
            merged_ranges.append([start,end])
    for start, end in merged_ranges:
        count += end - start + 1
    return count

# example_input: 3
# input: 643
with open(FILE_NAME, 'r') as file:
    lines = file.readlines()
    print("Part 1:", count_fresh([l.strip() for l in lines]))

with open(FILE_NAME, 'r') as file:
    lines = file.readlines()
    print("Part 1:", count_fresh_2([l.strip() for l in lines]))