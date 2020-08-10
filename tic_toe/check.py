def check_value(mapping,cell):
    row=cell[0]
    column=cell[1]-1
    already_played=True
    if(mapping[row][column]!=' '):
        print("cell already played")
        return already_played
    else:
        already_played=False
        return already_played

def check_full_board(mapping):
    for item in mapping.values():
        for i in item:
            if i!=' ':
                pass
            else:
                return False
    return True

def win_check(board,marks):
    for mark in marks:
        if((board['1'][0]==board['1'][1]==board['1'][2]==mark)or(board['1'][0]==board['2'][1]==board['3'][2]==mark)or(board['1'][0]==board['2'][0]==board['3'][0]==mark)or(board['1'][1]==board['2'][1]==board['3'][1]==mark)or(board['1'][2]==board['2'][2]==board['3'][2]==mark)or(board['2'][0]==board['2'][1]==board['2'][2]==mark)or(board['3'][0]==board['3'][1]==board['3'][2]==mark)or(board['1'][2]==board['2'][1]==board['3'][0]==mark)):
            win=True
            print(f'{mark} is the winner')
            return win
        else:
            win=False
    return win

if __name__=="__main__":
    print("This module is tested")