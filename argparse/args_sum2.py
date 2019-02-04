import argparse

parser = argparse.ArgumentParser()  #создаем объект класса ArgumentParser из модуля argparse
parser.add_argument('a') #добавляем аргумент
parser.add_argument('b') #добавляем аргумент

if len(sys.argv)==2:
    print('TOO FEW PARAMS')
elif len(sys.argv)>3:
    print('TOO MUCH PARAMS')
elif len(sys.argv)<2:
    print('NO PARAMS')
else:
    args = parser.parse_args() 
    s=int(args.a)+int(args.b)
    print(s)
