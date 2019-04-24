# Table of squared numbers

def squared():
    line = []
    for i in range(11,100):
        if i % 10 != 0:
            if i*i < 1000:
                if i == 19 or i == 29:
                    line.append(i*i)
                else:
                    line.append(str(i*i)+' ')
            else:
                line.append(i*i)
        else:
            print(*line)
            line = []
        
            

squared()
