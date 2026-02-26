import random

board = [" " for _ in range(9)]
def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8], 
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]          
    ]
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Position already taken.")
        except:
            print("Invalid input.")
def ai_move():
    print("Computer is thinking...")
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"
def main():
    print("🤖 CodSoft Tic Tac Toe AI")
    print("You = X | Computer = O")

    print_board()

    while True:

        player_move()
        print_board()

        if check_winner("X"):
            print("🎉 You win!")
            break

        if check_draw():
            print("It's a draw!")
            break

        ai_move()
        print_board()

        if check_winner("O"):
            print("Computer wins!")
            break

        if check_draw():
            print("It's a draw!")
            break

main()
