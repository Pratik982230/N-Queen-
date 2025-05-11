knight_moves = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

def is_safe_knight_tour(x, y, board, N):
    # A cell is safe if it's within bounds and hasn't been visited yet
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def count_onward_moves(x, y, board, N):
    # Count available moves from the next position (x, y)
    count = 0
    for move in knight_moves:
        next_x = x + move[0]
        next_y = y + move[1]
        if is_safe_knight_tour(next_x, next_y, board, N):
            count += 1
    return count

def next_move_heuristic(x, y, board, N):
    # Find the next knight's move using Warnsdorff's heuristic
    min_deg_idx = -1
    min_deg = float('inf')
    start_x, start_y = x, y
    
    # Try all the moves from the current position
    for i, move in enumerate(knight_moves):
        next_x = start_x + move[0]
        next_y = start_y + move[1]
        if is_safe_knight_tour(next_x, next_y, board, N):
            degree = count_onward_moves(next_x, next_y, board, N)
            if degree < min_deg:
                min_deg = degree
                min_deg_idx = i

    # Return the move with the fewest onward moves
    return knight_moves[min_deg_idx] if min_deg_idx != -1 else None

def solve_knight_tour_util(x, y, movei, board, N, steps):
    # Base case: all squares are visited
    if movei == N * N:
        return True

    # Get the next move using Warnsdorff's heuristic
    next_move = next_move_heuristic(x, y, board, N)
    if not next_move:
        return False

    next_x = x + next_move[0]
    next_y = y + next_move[1]

    # Try the selected move
    if is_safe_knight_tour(next_x, next_y, board, N):
        board[next_x][next_y] = movei
        steps.append([row[:] for row in board])  # Save the board state

        if solve_knight_tour_util(next_x, next_y, movei + 1, board, N, steps):
            return True

        # Backtrack
        board[next_x][next_y] = -1
        steps.append([row[:] for row in board])  # Save backtrack step

    return False

def solve_knight_tour(N):
    # Initialize the board with -1 (indicating unvisited cells)
    board = [[-1 for _ in range(N)] for _ in range(N)]
    steps = []

    # Start knight at the top-left corner (0, 0)
    board[0][0] = 0
    steps.append([row[:] for row in board])  # Save the initial state

    if not solve_knight_tour_util(0, 0, 1, board, N, steps):
        return []  # Return empty if no solution is found
    else:
        return steps
