X = 'X'
O = 'O'

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board: list):
    line = '---+---+---' 
    print(line)
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]}')
        print(line)
    


def get_input(index):
    while True:
        try:
            inputs = int(input(f'Enter a {index} (0-2): '))
            if 0 <= inputs <= 2:
                return inputs
            raise ValueError
        except ValueError:
            print('Invalid Input')

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
        
    for column in range(3):
            if board[0][column] == board[1][column] == board[2][column] != ' ':
                return True
        
    if (board[0][0] == board[1][1] == board[2][2] != ' ' 
           or board[2][0] == board[1][1] == board[0][2] != ' '):
            return True

    return False    


def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    
    return True

def main():
    current_player = X
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn")
        row = get_input('Row')
        column = get_input('Column')

        if board[row][column] == ' ':
            board[row][column] = current_player
        else: 
            print('This spot is already taken')
            continue

        print_board(board)

        if (check_winner(board)):
            print('Player {current_player} wins!')

        if is_full(board):
            print('The board is Full!')
            break

        current_player = X if current_player == O else O

if __name__ == '__main__':
    main()