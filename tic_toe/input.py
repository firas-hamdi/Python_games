'''
    This module contains functions that ask from the user to input data
'''

def input_cell():
    '''
    Function to define a cell coordinates in the board
    It returns a list containing the coordinates
    '''
    position = []
    row = ''
    column = ''
    accepted_row_values = ['1', '2', '3']
    accepted_column_values = [1, 2, 3]
    #  Ask the user to input the row number
    while row not in accepted_row_values:
        row = input("Input the desired line")
        if row not in accepted_row_values:
            print("Sorry, wrong line!")
    position.append(row)
    #  Ask the user to input the column number
    while not (column.isdigit()) or (int(column) not in accepted_column_values):
        column = input("Input the desired column")
        if not column.isdigit():
            print("Sorry input a digit ")
        else:
            if int(column) not in accepted_column_values:
                print("Sorry input a digit between 1 and 3")
    position.append(int(column))
    return position

def input_number():
    '''
    Function to define a number between 0 and 2
    It returns the chosen number
    '''
    while True:
        try:
            result = ''
            #  Ask the user to input a number between 0 and 2
            while result not in range(0, 3):
                result = int(input("input a number"))
                if result not in range(0, 3):
                    print("Please tap a number between 0 and 2")
        except TypeError:
            #   Exception thrown in case the user's input is not a digit 
            print("Try another number")
            continue
        else:
            #  Message mentioning the correct input
            print("good choice")
            break
    return result

if __name__ == "__main__":
    print("This module is tested")
    input_cell()
    input_number()