import collections

FILE_NAME = "input.txt"
# List of coordinate pairs for the 8 adjacent positions for a cell in a 2d grid
DIRECTIONS = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]


# Accessible rolls have less than 4 neighbors in the 8 adjacent spaces around them
def count_accessible_rolls(grid):
    # Get the size of the grid
    rows, cols = len(grid), len(grid[0])
    # Tracker for the amount of accessible grids
    count = 0

    # Traverse each element of the grid
    for r in range(rows):
        for c in range(cols):
            # Only check rolls, ie. "@"
            if grid[r][c] == "@":
                # Tracker for the amount of neighbors
                neighbor_count = 0
                # Check each of the 8 neighbors
                for dr, dc in DIRECTIONS:
                    r_, c_ = r + dr, c + dc
                    # If the neighbor is also a roll, increase neighbor_count
                    if r_ in range(rows) and c_ in range(cols) and grid[r_][c_] == "@":
                        neighbor_count += 1
                # Increment the count of rolls if the neighbor count is less than four
                if neighbor_count < 4:
                    count += 1
    # Return the total count
    return count


# Count the total number of accessible rolls removed
def count_total_removed_rolls(grid):
    # Get the size of the grid
    rows, cols = len(grid), len(grid[0])
    # Tracker for the total amount of rolls removed
    total_removed = 0
    # Tracker for the previous count of rolls removed
    # If 0, that means all accessible rolls have been removed
    prev_count = None
    while prev_count != 0:
        # Tracker for the amount of rolls removed in this pass
        current_count = 0
        # Traverse each element of the grid
        for r in range(rows):
            for c in range(cols):
                # Only check rolls, ie. "@"
                if grid[r][c] == "@":
                    # Tracker for neighbor counts
                    neighbor_count = 0
                    # Check each of the 8 neighbors
                    for dr, dc in DIRECTIONS:
                        r_, c_ = r + dr, c + dc
                        # If the neighbor is also a roll, increase neighbor_count
                        if (
                            r_ in range(rows)
                            and c_ in range(cols)
                            and grid[r_][c_] == "@"
                        ):
                            neighbor_count += 1
                    # If the total neighbor count is less than 3
                    # increment the removed roll count
                    # and set that space to removed, ie. "."
                    if neighbor_count < 4:
                        current_count += 1
                        grid[r][c] = "."
        # Add the current count to the total
        total_removed += current_count
        # Set prev to current count for the next iteration
        prev_count = current_count
    # Return total
    return total_removed


with open(FILE_NAME, "r") as file:
    lines = file.readlines()
    print("Part 1:", count_accessible_rolls([list(l.strip()) for l in lines]))

with open(FILE_NAME, "r") as file:
    lines = file.readlines()
    print("Part 2:", count_total_removed_rolls([list(l.strip()) for l in lines]))
