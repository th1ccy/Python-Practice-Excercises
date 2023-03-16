from IPython.display import clear_output
import random

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def player_input():
    
    validation_list = ['X', 'x', 'O', 'o']
    p1_marker = 'Empty'
    
    while p1_marker not in validation_list:
        p1_marker = input("Player 1 choose X or O: ")
        
        if p1_marker not in validation_list:  
            print ("\nThat is not a valid choice. Please try again.")
              
    else:
        print(f'\nPlayer 1 has chosen {p1_marker.upper()}')
    
    if p1_marker.upper() == 'X': 
        p2_marker = 'O'
        
    else:
        p2_marker = 'X'

    print(f'\nPlayer 2 will be {p2_marker}')
        
    return p1_marker.upper(), p2_marker.upper()

    
def place_marker(board, marker, position):
    board[position] = marker
    return board
    


def win_check(board, mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #Horizontal 1
    (board[4] == mark and board[5] == mark and board[6] == mark) or #Horizontal 2
    (board[7] == mark and board[8] == mark and board[9] == mark) or #Horizontal 3
    (board[1] == mark and board[4] == mark and board[7] == mark) or #Vertical 1
    (board[2] == mark and board[5] == mark and board[8] == mark) or #Vertical 2
    (board[3] == mark and board[6] == mark and board[9] == mark) or #Vertical 3
    (board[3] == mark and board[5] == mark and board[7] == mark) or #Diagonal 1
    (board[1] == mark and board[5] == mark and board[9] == mark))  #Diagonal 2



def choose_first():
    return str(random.randint(1,2)) 



def space_check(board, position):
    return board[position].isdigit()



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))      
    return position    
        

def replay():
    validation_list = ['Y', 'y', 'N', 'n']
    replay = 'EMPTY'
    
    while replay not in validation_list:
        replay = input('Would you like to paly again?(Y or N): ')
        if replay.upper() == 'Y':
            return True
        elif replay.upper() == 'N':
            return False
        else:
            print ('Invalid Input!')



print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('Player ' + turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.upper()[0] == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == '1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = '2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = '1'

    if not replay():
        break