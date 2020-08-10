def choose_side():
    side=''
    accepted_side_values=['X','O']
    while side.upper() not in accepted_side_values:
        side=input("Choose which side you want to play: O or X ")
        if side.upper() not in accepted_side_values:
            print("This is Tic Tac Toe, you can only choose X or O")
    if side.upper()=='X':
        player1='X'
        player2='O'
        return player1,player2
    else:
        player1='O'
        player2='X'
        return player1,player2

if __name__=="__main__":
    print("This module is tested")