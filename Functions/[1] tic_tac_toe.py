Text TicTacToe

def tic_tac_toe(field):

    def winner(line):
        if line.count('x') == 3 or line.count('0') == 3:
            return str(line[0]) + ' win'      
    k = True
    left_diagonal = [field[i][i] for i in range(3)]
    right_diagonal = [field[2- i][i] for i  in range(3)]
    
    
    for i in field:
        if winner(i):
            print(winner(i))
            k = False
            break
    if k:
        for i in range(len(field)):
            col = []
            for j in range(len(field[i])):
                col.append(field[j][i])
            if winner(col):
                print(winner(col))
                k = False
                break    
    if k:
        if winner(left_diagonal):
            winner(left_diagonal)
        elif winner(right_diagonal):
            winner(right_diagonal)
        else:
             print('draw')   
  



data = """0 x 0
x x x
x x -"""
field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)
