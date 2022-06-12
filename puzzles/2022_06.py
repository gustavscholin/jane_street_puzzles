"""Solution for Jane Street puzzle June 2022, Block Party 4

Unfortunately the current solution only works in theory, the time complexity
is too large. The example puzzle is solved instantly but the main puzzle isn't
(8h on my laptop wasn't enough...).

However, if I started solving the puzzle manually to reduce the search space
the algorithm could easily do the rest when I got stuck.
"""

from collections import Counter

Board = dict[tuple[int, int], int]


def check_region(val: int, i: int, j: int) -> bool:
    region = regions[(i, j)]
    region_vals = [
        board[coord] for coord, v in regions.items() if v == region and coord != (i, j)
    ]
    return val not in region_vals


def get_region_size(i: int, j: int) -> int:
    return region_sizes[regions[(i, j)]]


def taxi_distance(pos_1: tuple[int, int], pos_2: tuple[int, int]) -> int:
    return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])


def get_min_taxi_dist(i: int, j: int) -> bool:
    val = board[(i, j)]
    taxi_dists = [
        taxi_distance((i, j), alt_pos)
        for alt_pos, alt_val in board.items()
        if alt_val == val and alt_pos != (i, j)
    ]
    if taxi_dists:
        return min(taxi_dists)
    return None


def get_available_taxi_coords(i: int, j: int) -> list[tuple[int, int]]:
    val = board[(i, j)]
    return [
        alt_pos
        for alt_pos, alt_val in board.items()
        if alt_val is None and taxi_distance((i, j), alt_pos) == val
    ]


def solve(i: int, j: int) -> bool:
    next_i = i if j < board_size - 1 else i + 1
    next_j = j + 1 if j < board_size - 1 else 0

    if i < board_size:
        if not board[(i, j)]:
            for val in range(1, get_region_size(i, j) + 1):
                if check_region(val, i, j):
                    board[(i, j)] = val
                    min_taxi_dist = get_min_taxi_dist(i, j)
                    if not min_taxi_dist or min_taxi_dist > val:
                        available_taxi_coords = get_available_taxi_coords(i, j)
                        if not available_taxi_coords:
                            continue
                        for coord in available_taxi_coords:
                            board[coord] = val
                            if solve(next_i, next_j):
                                return True
                            board[coord] = None
                    elif min_taxi_dist < val:
                        continue
                    else:
                        if solve(next_i, next_j):
                            return True
            board[(i, j)] = None
            return False
        else:
            val = board[(i, j)]
            if check_region(val, i, j):
                min_taxi_dist = get_min_taxi_dist(i, j)
                if not min_taxi_dist or min_taxi_dist > val:
                    available_taxi_coords = get_available_taxi_coords(i, j)
                    if not available_taxi_coords:
                        return False
                    for coord in available_taxi_coords:
                        board[coord] = val
                        if solve(next_i, next_j):
                            return True
                        board[coord] = None
                    return False
                elif min_taxi_dist < val:
                    return False
                else:
                    return solve(next_i, next_j)
            else:
                return False
    return True


if __name__ == "__main__":
    """ """
    board_size = 10
    board = {
        (0, 0): None,
        (1, 0): None,
        (2, 0): None,
        (3, 0): None,
        (4, 0): 6,
        (5, 0): None,
        (6, 0): None,
        (1, 1): None,
        (2, 1): None,
        (3, 1): None,
        (0, 1): 3,
        (0, 2): None,
        (0, 3): None,
        (1, 2): None,
        (1, 3): 4,
        (1, 4): None,
        (0, 4): None,
        (0, 5): 7,
        (0, 6): None,
        (0, 7): None,
        (0, 8): None,
        (0, 9): None,
        (1, 5): None,
        (1, 8): None,
        (1, 9): None,
        (1, 6): None,
        (1, 7): None,
        (2, 7): None,
        (2, 2): None,
        (2, 3): None,
        (3, 3): 1,
        (2, 4): None,
        (2, 5): None,
        (2, 6): None,
        (3, 5): None,
        (3, 6): None,
        (3, 7): None,
        (4, 7): None,
        (4, 8): None,
        (2, 8): 2,
        (2, 9): None,
        (3, 8): None,
        (3, 9): None,
        (4, 9): None,
        (5, 8): None,
        (5, 9): 6,
        (3, 2): None,
        (4, 1): None,
        (4, 2): 1,
        (5, 2): None,
        (3, 4): None,
        (4, 3): None,
        (4, 4): None,
        (4, 5): None,
        (5, 5): None,
        (4, 6): None,
        (5, 1): None,
        (5, 3): None,
        (6, 3): None,
        (6, 4): None,
        (6, 5): None,
        (7, 4): None,
        (5, 4): None,
        (5, 6): None,
        (5, 7): 3,
        (6, 6): 2,
        (6, 1): None,
        (7, 0): None,
        (7, 1): 2,
        (8, 0): None,
        (8, 1): None,
        (8, 2): None,
        (9, 0): None,
        (9, 1): None,
        (9, 2): None,
        (9, 3): None,
        (6, 2): None,
        (7, 2): None,
        (6, 7): None,
        (6, 8): None,
        (6, 9): None,
        (7, 3): None,
        (8, 3): None,
        (8, 4): None,
        (9, 4): 5,
        (9, 5): None,
        (7, 5): None,
        (7, 6): None,
        (7, 9): None,
        (8, 5): None,
        (8, 6): 6,
        (8, 9): None,
        (9, 6): None,
        (9, 7): None,
        (9, 8): 2,
        (9, 9): None,
        (7, 7): None,
        (7, 8): None,
        (8, 7): None,
        (8, 8): None,
    }
    regions = {
        (0, 0): 0,
        (1, 0): 0,
        (2, 0): 0,
        (3, 0): 0,
        (4, 0): 0,
        (5, 0): 0,
        (6, 0): 0,
        (1, 1): 0,
        (2, 1): 0,
        (3, 1): 0,
        (0, 1): 1,
        (0, 2): 1,
        (0, 3): 1,
        (1, 2): 1,
        (1, 3): 1,
        (1, 4): 1,
        (0, 4): 2,
        (0, 5): 2,
        (0, 6): 2,
        (0, 7): 2,
        (0, 8): 2,
        (0, 9): 2,
        (1, 5): 2,
        (1, 8): 2,
        (1, 9): 2,
        (1, 6): 3,
        (1, 7): 3,
        (2, 7): 3,
        (2, 2): 4,
        (2, 3): 4,
        (3, 3): 4,
        (2, 4): 5,
        (2, 5): 5,
        (2, 6): 6,
        (3, 5): 6,
        (3, 6): 6,
        (3, 7): 6,
        (4, 7): 6,
        (4, 8): 6,
        (2, 8): 7,
        (2, 9): 7,
        (3, 8): 7,
        (3, 9): 7,
        (4, 9): 7,
        (5, 8): 7,
        (5, 9): 7,
        (3, 2): 8,
        (4, 1): 8,
        (4, 2): 8,
        (5, 2): 8,
        (3, 4): 9,
        (4, 3): 9,
        (4, 4): 9,
        (4, 5): 10,
        (5, 5): 10,
        (4, 6): 11,
        (5, 1): 12,
        (5, 3): 13,
        (6, 3): 13,
        (6, 4): 13,
        (6, 5): 13,
        (7, 4): 13,
        (5, 4): 14,
        (5, 6): 15,
        (5, 7): 15,
        (6, 6): 15,
        (6, 1): 16,
        (7, 0): 16,
        (7, 1): 16,
        (8, 0): 16,
        (8, 1): 16,
        (8, 2): 16,
        (9, 0): 16,
        (9, 1): 16,
        (9, 2): 16,
        (9, 3): 16,
        (6, 2): 17,
        (7, 2): 17,
        (6, 7): 18,
        (6, 8): 18,
        (6, 9): 18,
        (7, 3): 19,
        (8, 3): 19,
        (8, 4): 19,
        (9, 4): 19,
        (9, 5): 19,
        (7, 5): 20,
        (7, 6): 21,
        (7, 9): 21,
        (8, 5): 21,
        (8, 6): 21,
        (8, 9): 21,
        (9, 6): 21,
        (9, 7): 21,
        (9, 8): 21,
        (9, 9): 21,
        (7, 7): 22,
        (7, 8): 22,
        (8, 7): 22,
        (8, 8): 22,
    }

    partly_solved_board = {
        (0, 0): None,
        (0, 1): 3,
        (0, 2): 6,
        (0, 3): 5,
        (0, 4): 3,
        (0, 5): 7,
        (0, 6): None,
        (0, 7): None,
        (0, 8): 6,
        (0, 9): 5,
        (1, 0): None,
        (1, 1): None,
        (1, 2): 2,
        (1, 3): 4,
        (1, 4): 1,
        (1, 5): 1,
        (1, 6): 2,
        (1, 7): 3,
        (1, 8): 8,
        (1, 9): 2,
        (2, 0): None,
        (2, 1): None,
        (2, 2): 3,
        (2, 3): 2,
        (2, 4): 1,
        (2, 5): 2,
        (2, 6): 5,
        (2, 7): 1,
        (2, 8): 2,
        (2, 9): 4,
        (3, 0): None,
        (3, 1): None,
        (3, 2): 2,
        (3, 3): 1,
        (3, 4): 2,
        (3, 5): 6,
        (3, 6): 3,
        (3, 7): 1,
        (3, 8): 1,
        (3, 9): 3,
        (4, 0): 6,
        (4, 1): 3,
        (4, 2): 1,
        (4, 3): 1,
        (4, 4): 3,
        (4, 5): 2,
        (4, 6): 1,
        (4, 7): 4,
        (4, 8): 2,
        (4, 9): 7,
        (5, 0): 1,
        (5, 1): 1,
        (5, 2): 4,
        (5, 3): 5,
        (5, 4): 1,
        (5, 5): 1,
        (5, 6): 1,
        (5, 7): 3,
        (5, 8): 5,
        (5, 9): 6,
        (6, 0): 3,
        (6, 1): None,
        (6, 2): 2,
        (6, 3): 3,
        (6, 4): 2,
        (6, 5): 4,
        (6, 6): 2,
        (6, 7): 1,
        (6, 8): 2,
        (6, 9): 3,
        (7, 0): None,
        (7, 1): 2,
        (7, 2): 1,
        (7, 3): None,
        (7, 4): 1,
        (7, 5): 1,
        (7, 6): 3,
        (7, 7): 1,
        (7, 8): 4,
        (7, 9): 9,
        (8, 0): None,
        (8, 1): None,
        (8, 2): None,
        (8, 3): 4,
        (8, 4): None,
        (8, 5): 1,
        (8, 6): 6,
        (8, 7): 2,
        (8, 8): 3,
        (8, 9): 8,
        (9, 0): None,
        (9, 1): 6,
        (9, 2): None,
        (9, 3): None,
        (9, 4): 5,
        (9, 5): None,
        (9, 6): 4,
        (9, 7): 7,
        (9, 8): 2,
        (9, 9): 5,
    }

    example_board_size = 5
    example_board = {
        (0, 0): None,
        (0, 1): None,
        (0, 2): None,
        (0, 3): None,
        (0, 4): None,
        (1, 0): None,
        (1, 1): None,
        (1, 2): None,
        (1, 3): None,
        (1, 4): 2,
        (2, 0): None,
        (2, 1): None,
        (2, 2): 4,
        (2, 3): None,
        (2, 4): None,
        (3, 0): 3,
        (3, 1): None,
        (3, 2): None,
        (3, 3): None,
        (3, 4): None,
        (4, 0): None,
        (4, 1): None,
        (4, 2): None,
        (4, 3): None,
        (4, 4): None,
    }
    example_regions = {
        (0, 0): 0,
        (0, 1): 0,
        (0, 2): 1,
        (0, 3): 1,
        (0, 4): 1,
        (1, 0): 2,
        (1, 1): 0,
        (1, 2): 0,
        (1, 3): 3,
        (1, 4): 1,
        (2, 0): 2,
        (2, 1): 4,
        (2, 2): 0,
        (2, 3): 5,
        (2, 4): 1,
        (3, 0): 2,
        (3, 1): 6,
        (3, 2): 6,
        (3, 3): 5,
        (3, 4): 5,
        (4, 0): 2,
        (4, 1): 2,
        (4, 2): 6,
        (4, 3): 7,
        (4, 4): 5,
    }

    # Run solve algorithm on partly solved board
    board = partly_solved_board

    # Uncomment to run the smaller example
    # board_size = example_board_size
    # board = example_board
    # regions = example_regions

    region_sizes = Counter(regions.values())
    print(f"Solved: {solve(0, 0)}")
    print("Board:")
    print(board)
    products = []
    for i in range(board_size):
        product = 1
        for j in range(board_size):
            product *= board[(i, j)]
        products.append(product)
    print(f"Final answer: {sum(products)}")
