"""Solution for Jane Street puzzle July 2022, Andy's Morning Stroll"""
import random

import numpy as np

if __name__ == "__main__":
    # Calculate expected steps on the football
    P = np.zeros((20, 20))
    P[0, [1, 2, 19]] = 1 / 3
    P[1, [0, 4, 12]] = 1 / 3
    P[2, [0, 3, 9]] = 1 / 3
    P[3, [2, 4, 5]] = 1 / 3
    P[4, [1, 3, 6]] = 1 / 3
    P[5, [3, 7, 10]] = 1 / 3
    P[6, [4, 7, 8]] = 1 / 3
    P[7, [5, 6, 11]] = 1 / 3
    P[8, [6, 12, 14]] = 1 / 3
    P[9, [2, 10, 15]] = 1 / 3
    P[10, [5, 9, 13]] = 1 / 3
    P[11, [7, 13, 14]] = 1 / 3
    P[12, [1, 8, 18]] = 1 / 3
    P[13, [10, 11, 16]] = 1 / 3
    P[14, [8, 11, 17]] = 1 / 3
    P[15, [9, 16, 19]] = 1 / 3
    P[16, [13, 15, 17]] = 1 / 3
    P[17, [14, 16, 18]] = 1 / 3
    P[18, [12, 17, 19]] = 1 / 3
    P[19, [0, 15, 18]] = 1 / 3

    expected_nbr_steps = round(1 / np.linalg.matrix_power(P, 1000)[0, 0])
    print(f"Calculated expected number of steps on football: {expected_nbr_steps}")

    # Simulation to verify result
    steps = []

    for _ in range(10_000):
        start = 0
        state = np.random.choice(20, 1, p=P[start])[0]
        step = 1

        while state != start:
            state = np.random.choice(20, 1, p=P[state])[0]
            step += 1

        steps.append(step)

    print(f"Simulated number of steps on football: {sum(steps) / len(steps)}")

    # Calculate p
    p = 1

    def move(coord, dir, steps):
        global p
        if (
            steps > expected_nbr_steps
            or abs(coord[0]) + steps > expected_nbr_steps
            or abs(coord[1]) + steps > expected_nbr_steps
        ):
            return
        elif coord == (0, 0) and steps > 0:
            p -= (1 / 3) ** steps
            return
        if dir == "down":
            move((coord[0] + 1, coord[1]), "up", steps + 1)
            move((coord[0], coord[1] - 1), "up", steps + 1)
            move((coord[0] - 1, coord[1] + 1), "up", steps + 1)
        elif dir == "up":
            move((coord[0] - 1, coord[1]), "down", steps + 1)
            move((coord[0], coord[1] + 1), "down", steps + 1)
            move((coord[0] + 1, coord[1] - 1), "down", steps + 1)

    move((0, 0), "down", 0)
    print(f"Calculated p: {p}")

    # Simulation to verify result
    simulations = 1_000_000
    over_expected_nbr_steps = 0

    for _ in range(simulations):
        coord = (0, 0)
        dir = "down"
        steps = 0

        while True:
            if (
                steps > expected_nbr_steps
                or abs(coord[0]) + steps > expected_nbr_steps
                or abs(coord[1]) + steps > expected_nbr_steps
            ):
                over_expected_nbr_steps += 1
                break
            elif coord == (0, 0) and steps > 0:
                break

            if dir == "down":
                coord = random.choice(
                    [
                        (coord[0] + 1, coord[1]),
                        (coord[0], coord[1] - 1),
                        (coord[0] - 1, coord[1] + 1),
                    ]
                )
            elif dir == "up":
                coord = random.choice(
                    [
                        (coord[0] - 1, coord[1]),
                        (coord[0], coord[1] + 1),
                        (coord[0] + 1, coord[1] - 1),
                    ]
                )

            dir = "up" if dir == "down" else "down"
            steps += 1

    print(f"Simulated p: {over_expected_nbr_steps / simulations}")
