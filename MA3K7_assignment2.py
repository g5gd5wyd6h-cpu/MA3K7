import numpy as np
import random

def determinant_game(n, first_turn, silent=False):

    # Initialise the n x n matrix, -1 represents unfilled
    matrix = np.full((n, n), -1)

    # Pair rows as in rubric, (1st,2nd), (3rd, 4th), etc.
    pairs = [(i, i+1) for i in range(0, n, 2)]

    # return the paired row
    def paired_row(i):
        for r1, r2 in pairs:
            if i == r1: return r2
            if i == r2: return r1

    # simulate opponent move
    def opponent_move():
        unfilled = list(zip(*np.where(matrix == -1)))  # all empty coordinates
        if unfilled:
            r, c = random.choice(unfilled)
            matrix[r, c] = 1
            return r, c


    # 0-player move
    def zero_move(opponent_r, opponent_c):
        r = paired_row(opponent_r)
        if matrix[r, opponent_c] == -1:
            matrix[r, opponent_c] = 0
        else:
            # dont play in a paired blank and check if its already been played in
            unfilled = list(zip(*np.where(matrix == -1)))  # all empty coordinates
            if unfilled:
                r, c = random.choice(unfilled)
                while (matrix[paired_row(r),c] == 0):
                    r, c = random.choice(unfilled)
                matrix[r, c] = 0
                return


    # if the opponent goes first
    if first_turn == "opponent":
        r, c = opponent_move()
        zero_move(r, c)
    # if the player goes first
    elif first_turn == "player":
        r = random.randint(0, n-1)
        c = random.randint(0, n-1)
        matrix[r, c] = 0

    while np.any(matrix == -1):
        r, c = opponent_move()
        if np.any(matrix == -1):
            zero_move(r, c)

    if not silent:
        print("Final matrix:")
        print(matrix)
        print("Determinant:", round(np.linalg.det(matrix)))

    if (round(np.linalg.det(matrix)) != 0):
        print("Final matrix:")
        print(matrix)
        print("Determinant:", round(np.linalg.det(matrix)))
    return round(np.linalg.det(matrix))


# Example:
print("Example final game state:")
determinant_game(8, "opponent")

#do it 1000 times
print("Running 1000 simulations...")
count = 0
for q in range (0, 1000):
    sizes = [4,6,8,10]
    turns = ["player", "opponent"]
    det = determinant_game(random.choice(sizes), random.choice(turns), silent=True)
    if det == 0:
        count += 1

print("Final results:")
print("The player won ", count, "/ 1000 games.")