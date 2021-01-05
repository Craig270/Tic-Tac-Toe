##Test board and Game Board Design
from IPython.display import clear_output
test_board = ['#','X','O','X','O','X','O','X','O','X']
board = [' ']*10
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3]) 
##Players choose to be X or O in order to get started playing.   
def player_input():
    #Output 
    marker = ' '
    
    #Keep asking PLayer 1 to choose X or O 
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    #Assign PLayer to, the opposite marker 
    player1 = marker 
    
    if player1 == 'X':
        player2='O'
    else:
        player2='X'
    
    return (player1,player2) 

##Places X or O on the board. 
def place_marker(board, marker, position):
    
    board[position] = marker 
 
 
## Check to see if a player has won. boolean. 
def win_check(board, mark):
    #Win Tic Tax Toe? 
    
    #All Rows and check to see if they all share the same marker 
    return ((board[7]== mark and board[8]== mark and board[9]==mark) or
    (board[4]== mark and board[5]== mark and board[6]==mark) or
    (board[1]== mark and board[2]== mark and board[3]==mark) or
    
    
    #All COLUMNS, check to see if marker matches 
    (board[1]== mark and board[4]== mark and board[7]==mark) or
    (board[2]== mark and board[5]== mark and board[8]==mark) or
    (board[3]== mark and board[6]== mark and board[9]==mark) or
    
    
    #2 diagonals, check to see match
    (board[1]== mark and board[5]== mark and board[9]==mark) or
    (board[3]== mark and board[5]== mark and board[7]==mark))

import random

##What user goes first
def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2' 
##Look for empty spaces on the board.    
def space_check(board, position):
    
    return board[position] == ' ' 
##Look for a full board. boolean
def full_board_check(board):
    
    for i in range(1,10): 
        if space_check(board,i):
            return False
    return True
##Ask user where to place their marker.(X or O)
def player_choice(board): 
    
    position = 0
    
    while position not in list(range(1,10)) or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    
    return position 
##Ask to play again 
def replay():
    
    choice = input('Play again? Enter Yes or No: ')
    
    return choice == 'Yes'


########################TIC-TAC-TOE GAME ########################
#While Loop to keep running the Game

print('Welcome to Tic Tac Toe!')

while True:
    
    #Play the Game 
    
    ##Set everything up (Board, whos first, choose markers X,O)
    the_board = [' ']*10 
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? y or n: ')
    if play_game== 'y':
        game_on=True
    else: 
        game_on=False 
    
    ##Game Play
    
    while game_on:
        if turn == "Player 1":
            #show the board
            display_board(the_board)
            #Choose position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check (the_board,player1_marker):
                display_board(the_board)
                print('Player1 Has WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:            
            #show the board
            display_board(the_board)
            #Choose position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check (the_board,player2_marker):
                display_board(the_board)
                print('Player2 Has WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game Over! Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'   
#Break out of the while loop on no replay()    
    if not replay():
        break