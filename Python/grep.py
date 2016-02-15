#!/usr/bin/python3
import argparse
import re
import glob
import sys

parser = argparse.ArgumentParser(description='Grep')
parser.add_argument('pattern',type=str,help='Шаблон поиска')
parser.add_argument('-i',action='store_true',help='Игнорировать регистр')
parser.add_argument('-m',type=int,help='Остановиться после указанного числа совпадений')
parser.add_argument('-n',action='store_true',help='Печатать номер строки вместе с выходными строками')
parser.add_argument('-e',action='store_true',help='Шаблон - регулярное выражение')
parser.add_argument('files',metavar='file',type=str,nargs='*',help='файлы для обработки')

args = parser.parse_args()

def printuy(text,file='stdin'):
    how_match=0
    for i, line in enumerate(text):
        flag=False
        if (args.i and args.e):
            flag=re.search(args.pattern, line, re.IGNORECASE)
        elif args.e:
            flag=re.search(args.pattern,line)
        elif args.i:
            flag=args.pattern.lower() in line.lower()
        else:
            flag=args.pattern in line
        if flag:#(args.i and re.search(args.pattern, line, re.IGNORECASE)) or (re.search(args.pattern, line)):
            how_match+=1
            if args.m:
                if how_match > args.m:
                    break
            if args.n:
                print(file,i,':',line)
            else:
                print(file,line)

if args.files:
    for pattern in args.files:
        if len(glob.glob(pattern))==0:
            sys.stderr.write("Error while opening file" + "\n")
        else:
            for file in glob.iglob(pattern):
                printuy(open(file).readlines(),file)
else:
    printuy(sys.stdin.readlines())
                
