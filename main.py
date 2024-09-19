import time
from math import gcd
from collections import deque


def bfs_water_jug_solver(jug1, jug2, target, target_jug):
    # Check if the problem is solvable
    if target > max(jug1, jug2) or target % gcd(jug1, jug2) != 0:
        return "No solution possible."

    visited = set()
    queue = deque([((0, 0), [])])  # Initialize queue with state and path
    visited.add((0, 0))

    while queue:
        (current_a, current_b), path = queue.popleft()

        # Check if the current state has reached the target
        if (current_a == target and target_jug == 'A') or (current_b == target and target_jug == 'B'):
            return path + [(current_a, current_b, "Target achieved")]

        # Generate all possible states
        states = [
            (jug1, current_b, "Fill Jug A completely"),
            (current_a, jug2, "Fill Jug B completely"),
            (0, current_b, "Empty Jug A completely"),
            (current_a, 0, "Empty Jug B completely"),
            # Pour from A to B
            (current_a - min(current_a, jug2 - current_b), current_b + min(current_a, jug2 - current_b),
             "Pour from A to B"),
            # Pour from B to A
            (current_a + min(current_b, jug1 - current_a), current_b - min(current_b, jug1 - current_a),
             "Pour from B to A")
        ]

        for new_a, new_b, action in states:
            if (new_a, new_b) not in visited:
                visited.add((new_a, new_b))
                queue.append(((new_a, new_b), path + [(new_a, new_b, action)]))

    return "No solution possible."


# Input capacities and target from user
jug1_capacity = int(input("Enter capacity of Jug A: "))
jug2_capacity = int(input("Enter capacity of Jug B: "))
target_capacity = int(input("Enter target capacity: "))
target_jug = input("Which jug is the target (A or B)? ").upper()

# Validate target jug input
if target_jug not in ['A', 'B']:
    print("Error: Target jug must be 'A' or 'B'.")
else:
    # Solve the problem
    start_time = time.time()
    solution = bfs_water_jug_solver(jug1_capacity, jug2_capacity, target_capacity, target_jug)
    if isinstance(solution, list):
        print("Steps to achieve target:")
        for state in solution:
            print(f"Jug A: {state[0]} liters, Jug B: {state[1]} liters - Action: {state[2]}")
    else:
        print(solution)
    print(f"Time taken: {time.time() - start_time:.5f}seconds.")
