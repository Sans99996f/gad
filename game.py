def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Проверка строк
    for row in board:
        if all(s == player for s in row):
            return True
    # Проверка столбцов
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    for row in board:
        if any(s == " " for s in row):
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
        col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif check_tie(board):
                print_board(board)
                print("Ничья!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Эта клетка уже занята. Попробуйте снова.")

if __name__ == "__main__":
    main()
