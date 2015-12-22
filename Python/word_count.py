import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Word Count')
parser.add_argument('files',metavar='file',type=str,nargs='*',help='файлы для обработки')
parser.add_argument('-c',action='store_true',help='количество байт')
parser.add_argument('-m',action='store_true',help='количество символов')
parser.add_argument('-l',action='store_true',help='количество строк')
parser.add_argument('-w',action='store_true',help='количество слов')

args = parser.parse_args()      

def word_count(text):
	#количество байт
	c=sys.getsizeof(text)
	#количество символов
	m=len(text)
	#количество строк
	l=text.count('\n')+1
	#количество слов
	w=len(text.split())
	result=''
	if not (args.c or args.m or args.l or args.w):
		result=str(c)+' '+str(m)+' '+str(l)+' '+str(w)+' '
	if args.c:
		result+=str(c)+' '
	if args.m:
		result+=str(m)+' '
	if args.l:
		result+=str(l)+' '
	if args.w:
		result+=str(w)+' '
	return filename+' '+result

def count_file(filename):
	try:
		input=open(filename, 'r')
		text=input.read()
		input.close()
		return word_count(text)
	except IOError:
		print("File",filename,"not found!")

if args.files:
	for filename in args.files:
		print(count_file(filename))
else:
	print(word_count(sys.stdin.read()))



    
 