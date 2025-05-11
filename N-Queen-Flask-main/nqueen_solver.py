def is_safe_queen(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nq_util(board, col, N, steps):
    if col >= N:
        return True

    for i in range(N):
        if is_safe_queen(board, i, col, N):
            board[i][col] = 1
            steps.append([row[:] for row in board])

            if solve_nq_util(board, col + 1, N, steps):
                return True

            board[i][col] = 0  # Backtrack
            steps.append([row[:] for row in board])

    return False

def solve_n_queen(N):
    board = [[0] * N for _ in range(N)]
    steps = []
    solve_nq_util(board, 0, N, steps)
    return steps
