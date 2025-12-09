import math

DEBUG = False
FILE_NAME = "example_input.txt" if DEBUG else "input.txt"
N_CLOSEST = 10 if DEBUG else 1000

# Parse input as list of tuple coordinates
coords = [
    tuple(int(s) for s in l.strip().split(","))
    for l in open(FILE_NAME).read().splitlines()
]

# Calculate distances and save to dict where the key is 'p1_index,p2_index'
# so we can reference each point in the original coords list
distances_map = {}

# Iterate over each element, i, against the i+1 element to get their distance
for i in range(len(coords)):
    curr_i = coords[i]
    for j in range(i + 1, len(coords)):
        curr_j = coords[j]
        distance = math.dist(curr_i, curr_j)
        distances_map[str(i) + "," + str(j)] = distance

# Sort the distances from lowest to highest
sorted_distances = sorted(distances_map.items(), key=lambda c: c[1])
# Get the n most distances
shortest_distances = sorted_distances[:N_CLOSEST]
# Get the coordinate indexes from the n most distances
shortest_distances_coords = [s[0].split(",") for s in shortest_distances]
# Create circuits as sets for each coordinate index pair
circuits = [{p1, p2} for [p1, p2] in shortest_distances_coords]

# Merge circuits while possible
# Find common coordinate indexes and merge into set
while True:
    # Keep track of the previous amount of circuits
    prev_count = len(circuits)
    # Keep track of new circuits
    new_circuits = []
    # Traverse over the previous circuits
    for circuit in circuits:
        # Traverse for any new circuits made
        for existing in new_circuits:
            # If there as an overlap between the circuit and an existing circuit,
            # update the existing circuit to add new node
            if existing & circuit:
                existing.update(circuit)
                break
        # Otherwise, add the circuit back to the circuit
        else:
            new_circuits.append(circuit)
        # Set circuits to the new circuits
        circuits = new_circuits
        # If nothing has changed, exit
    if len(circuits) == prev_count:
        break

# Sort circuits by size from biggest to smallest
sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
# Multiply the sizes of the top 3
print(math.prod([len(c) for c in sorted_circuits[:3]]))

## Part 2
# Use all coordinates
all_coords = [s[0].split(",") for s in sorted_distances]
# Keep track of last connection made
last_connection = None
# Start with empty circuits
circuits = []

# Iterate over all coordinates to add connections one by one
for connection in all_coords:
    p1, p2 = connection
    circuits.append({p1, p2})
    # Merge circuits while possible
    # Find common coordinate indexes and merge into set
    while True:
        # Keep track of the previous amount of circuits
        prev_count = len(circuits)
        # Keep track of new circuits
        new_circuits = []
        # Traverse over the previous circuits
        for circuit in circuits:
            # Traverse for any new circuits made
            for existing in new_circuits:
                # If there as an overlap between the circuit and an existing circuit,
                # update the existing circuit to add new node
                if existing & circuit:
                    existing.update(circuit)
                    break
            # Otherwise, add the circuit back to the circuit
            else:
                new_circuits.append(circuit)
            # Set circuits to the new circuits
            circuits = new_circuits
            # If nothing has changed, exit
        if len(circuits) == prev_count:
            break
    # All coords will be connected when there is 1 circuit
    # and the size of that circuit is equal to the number of coords
    if len(circuits) == 1 and len(circuits[0]) == len(coords):
        last_connection = connection
        break

p1, p2 = [int(p) for p in last_connection]
coord1, coord2 = coords[p1], coords[p2]
# Multiply the two x values of the last connection
print(math.prod([coord1[0], coord2[0]]))
