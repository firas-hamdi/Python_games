'''
This program simulates the Tic Tac Toe game
'''
import random
import side
from input import input_cell
import check

def display(input1, input2, input3):
    '''
    Function to display the 3 given inputs
    '''
    print(input1)
    print(input2)
    print(input3)

def choose_first_player():
    '''
    Function to choose which player will start first
    It returns the player to start
    '''
    first_to_play = random.randint(1, 2)
    return first_to_play

def replace(mapping, cell, new_value):
    '''
    Function to replace the content of the cell chosen by the user into X or O
    It returns the new board after change
    '''
    row = cell[0]
    column = cell[1]-1
    mapping[row][column] = new_value
    return mapping

def game_continue():
    '''
    Function to ask the user if he/she wants to continue playing
    It returns a boolean (True for continuing the game, Flse for not)
    '''
    choice = 'wrong'
    accepted_value = ['Y', 'N']
    while choice.upper() not in accepted_value:
        choice = input("You want to keep playing? Y or N: ")
        if choice.upper() not in accepted_value:
            print("Sorry wrong answer. Yes or No question")
    if choice.upper() == 'Y':
        continue_game = True
    elif choice.upper() == 'N':
        continue_game = False
    return continue_game

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe") 
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    tic_toe_map = {'1':row1, '2':row2, '3':row3}
    display(tic_toe_map['1'], tic_toe_map['2'], tic_toe_map['3'])
    gameon = True
    already_played = True
    stop_game = False
    full_board = False
    while gameon:
        (player1, player2) = side.choose_side()
        first_player = choose_first_player()
        if first_player == 1:
            turn = player1
        else:
            turn = player2
        print(f"the first player is {turn}")
        while(not stop_game) and (not full_board):
            if turn == player1:
                print(f"{turn} turn")
                while already_played:
                    position = input_cell()
                    already_played = check.check_value(tic_toe_map, position)
                already_played = True
                replace(tic_toe_map, position, player1)
                display(tic_toe_map['1'], tic_toe_map['2'], tic_toe_map['3'])
                if check.win_check(tic_toe_map, ['X', 'O']):
                    stop_game = True
                    gameon = game_continue()
                    if gameon:
                        row1 = [' ', ' ', ' ']
                        row2 = [' ', ' ', ' ']
                        row3 = [' ', ' ', ' ']
                        tic_toe_map = {'1':row1, '2':row2, '3':row3}
                        stop_game = False
                        break
                    else:
                        print("Loser surrendered")
                else:
                    full_board = check.check_full_board(tic_toe_map)
                    if not full_board:
                        turn = player2
            if turn == player2:
                print(f"{turn} turn")
                while already_played:
                    position = input_cell()
                    already_played = check.check_value(tic_toe_map, position)
                already_played = True
                replace(tic_toe_map, position, player2)
                display(tic_toe_map['1'], tic_toe_map['2'], tic_toe_map['3'])
                if check.win_check(tic_toe_map, ['X', 'O']):
                    stop_game = True
                    gameon = game_continue()
                    if gameon:
                        row1 = [' ', ' ', ' ']
                        row2 = [' ', ' ', ' ']
                        row3 = [' ', ' ', ' ']
                        tic_toe_map = {'1':row1, '2':row2, '3':row3}
                        stop_game = False
                        break
                    else:
                        print("Loser surrendered")
                else:
                    full_board = check.check_full_board(tic_toe_map)
                    if not full_board:
                        turn = player1
        if full_board:
            gameon = game_continue()
            if gameon:
                row1 = [' ', ' ', ' ']
                row2 = [' ', ' ', ' ']
                row3 = [' ', ' ', ' ']
                tic_toe_map = {'1':row1, '2':row2, '3':row3}
                full_board = False
            else:
                print("It's good to leave on a draw ;) !!")

