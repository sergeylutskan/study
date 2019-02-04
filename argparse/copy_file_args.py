import argparse

parser = argparse.ArgumentParser()  #создаем объект класса ArgumentParser из модуля argparse
parser.add_argument('file1', type=argparse.FileType(mode='r')) #добавляем аргумент
parser.add_argument('file2', type=argparse.FileType(mode='w')) #добавляем аргумент
parser.add_argument('--upper', action='store_true') #добавляем аргумент
parser.add_argument('--lines', type=int) #добавляем аргумент

args = parser.parse_args() #
content=''

for i in range(args.lines):
    content=content+args.file1.readline()

if args.upper:
    content=content.upper()
args.file2.write(content)
