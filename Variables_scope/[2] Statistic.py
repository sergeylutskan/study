# Statistics of money transaction from text

def get_transactions(t, hist = {}):
    global transactions
    if t == 'print_it':
        for i in hist.keys():
            print(hist[i][1],i,hist[i][0])
    else:
        naznachenie = t[t.find('-')+1:t.find(':')]
        summa = t[t.find(':')+1:]
        if hist.get(naznachenie) == None:
            hist[naznachenie] = [int(summa),1]
        else:
            hist[naznachenie][0] = hist[naznachenie][0] + int(summa)
            hist[naznachenie][1] = hist[naznachenie][1] + 1
    
    transactions = hist    

get_transactions('880005553535-перевод:100')
get_transactions('111111111-перевод:1000')
get_transactions('880005553535-оплата_жкх:10000')
get_transactions('89065664312-перевод:50000000')
get_transactions('print_it')
