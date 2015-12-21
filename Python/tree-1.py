import os
import argparse

parser = argparse.ArgumentParser(description='Tree')
parser.add_argument('-d',action='store_true',help='List directories only')
parser.add_argument('-o',type=str,help='[filename]  Send output to filename')
parser.add_argument('-n',required=True,type=str,help='Path')

args = parser.parse_args()
 
def print_dir(path, otstup=''):
        if args.o:
                output=open(args.o, 'a')
                output.write(otstup+'├── (dir) '+os.path.basename(path)+'\n')
                output.close()
        else:
                print (otstup+'├── (dir)', os.path.basename(path))
        for name in os.listdir(path):
                fullname = os.path.join(path, name)
                if os.path.isdir(fullname):
                        print_dir(fullname, otstup + '│  ')
                elif not args.d:
                        if args.o:
                                output=open(args.o, 'a')
                                output.write(otstup+'│  ├── (file) '+name+'\n')
                                output.close()
                        else:
                                print (otstup+'│  ├── (file)', name)                

if args.o:
        output=open(args.o, 'w')
        output.close()
print_dir(args.n)