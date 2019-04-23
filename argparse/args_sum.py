# Сложение двух переданных аргументов
# Addition of the two arguments


import argparse

parser = argparse.ArgumentParser()  #создаем объект класса ArgumentParser из модуля argparse
parser.add_argument('a') #добавляем аргумент
parser.add_argument('b') #добавляем аргумент

args = parser.parse_args() #
s=int(args.a)+int(args.b)
print(s)
