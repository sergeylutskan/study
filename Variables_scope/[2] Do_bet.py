# Horse racing Bets 

def do_bet(a, b, h = {}):
    global horses
    if (a not in h.keys()) and (b != 0):
        h[a] = b
        print('Ваша ставка в размере ' + str(b) + ' на лошадь ' + str(a) + ' принята')
    else:
        print('Что-то пошло не так, попробуйте еще раз')
    horses = h    

do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)
