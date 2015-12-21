import mymodule
import sys


          
def how_many(file):
     try:
          f = open(file)
          s = f.read()
          return mymodule.how_many(s)
     except IOError:
          print("no file")
     finally:
          f.close()
file=sys.argv[-1]     
result = how_many(file)
for letter in result:
     print(letter, result[letter])

