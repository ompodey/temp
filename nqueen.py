def is_safe(board, row, col):
    # Check if there is a queen in the same row or diagonals
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True
def solve_n_queens(board, col, n):
    if col == n:
        return True
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            if solve_n_queens(board, col + 1, n):
                return True
    return False
def print_board(board):
    for row in board:
        print(' '.join(['Q' if i == row else '.' for i in range(len(board))]))
def main():
    n = int(input("Enter the value of n: "))
    # Initialize the board with the first queen already placed
    board = [0] * n
    board[0] = 0
    if solve_n_queens(board, 1, n):
        print("Solution exists. Here is the n-Queens matrix:")
        print_board(board)
    else:
        print("Solution does not exist.")
if __name__ == "__main__":
    main()

