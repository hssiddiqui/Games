# Tic Tac Toe played human vs computer

#global constraints
X = "X"
O = "O"
Empty = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    print("""
    TIC TAC TOE
    Make you move by entering a number 0-8. 
    The number will correspond to the board position as illustrated:
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
    """)


# Ask a yes or no question
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


#Ask for a number within a range
def ask_number(question, low, high):
    response = None
    while response not in range (low, high):
        response = int(input(question))
    print(response)
    return response


#Determine if the player or the computer goes first
def pieces():
    go_first = ask_yes_no("Do you want to go first? (y/n): ")
    if go_first == "y":
        print ("\n First move is yours.")
        human = X
        computer = O

    else:
        print("\n The computer goes first.")
        human = O
        computer = X

    return computer, human


#Create a new board game
def new_board():
    board=[]
    for square in range(NUM_SQUARES):
        board.append(Empty)
    return board


#Displaying the board
def display_board(board):
    print("\n\t\t", board[0], " | ", board[1], " | ", board[2])
    print("\t\t"," -----------")
    print("\t\t", board[3], " | ", board[4], " | ", board[5])
    print("\t\t", " -----------")
    print("\t\t", board[6], " | ", board[7], " | ", board[8],"\n")


#Create a list of legal moves
def legal_moves(board):
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square] == Empty:
            moves.append(square)
    return moves


#Determine the game winner
def winner(board):
    WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != Empty:
            winner = board[row[0]]
            return winner

        if Empty not in board:
            return TIE

    return None


# Get human move
def human_move(board,human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nIllegal move!\n")
    return move

# The computer move
def computer_move(board, computer, human):
    board = board[:] #Make a copy of the board
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("Computer takes square number : ",)

    # if computer can win take that move
    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move]=Empty

    # if human can win block that move
    for move in legal_moves(board):
        board[move]=human
        if winner(board)==human:
            print(move)
            return move
        #done checking this move, undo it
        board[move]=Empty

    # Since no one can win on the next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


# Switch turns
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

#Congratulate thw winner
def congrat_winner(the_winner,computer,human):
    if the_winner != TIE:
        print(the_winner, " won!\n")
    else:
        print("It's a tie!\n")
    if the_winner==human:
        print("Congratulations on the win!")
    if the_winner==computer:
        print("You'll win next time!")



# The main function
def main():
    display_instruct()
    computer,human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn==human:
            move = human_move (board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn=next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# Starting the program
main()
input("\n\nPress the enter key to exit.")
