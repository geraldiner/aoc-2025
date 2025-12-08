# FILE_NAME = "example_input.txt"
FILE_NAME = "input.txt"

lines = [list(l.strip()) for l in open(FILE_NAME).read().splitlines()]
rows, cols = len(lines), len(lines[0])

# Part 1
# 21
# 1687
p1 = 0
# Part 2
# 40
# 390684413472684
timelines = [0] * cols
for r in range(rows):
    for c in range(cols):
        char = lines[r][c]
        if char == "S":
            lines[r][c] = "|"
            timelines[c] = 1
        elif lines[r - 1][c] == "|":
            if char == "^":
                lines[r][c - 1] = "|"
                lines[r][c + 1] = "|"
                p1 += 1
                timelines[c - 1] += timelines[c]
                timelines[c + 1] += timelines[c]
                timelines[c] = 0
            else:
                lines[r][c] = "|"
print(p1)
print(sum(timelines))
