class Stack:
     def __init__(self):
          self.items = []
         
     def isEmpty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def size(self):
          return len(self.items)
     
def rpn(string):
     s=Stack()
     i=0
     helper_list=string.split(" ")
     for elem in helper_list:
          if elem.isdigit():
               s.push(int(elem))
          elif elem == "+":
               s.push(s.pop()+s.pop())
          elif elem == "*":
               s.push(s.pop()*s.pop())
          elif elem == "-":
               s.push(s.pop()-s.pop())
          elif elem == "_":
               s.push(s.pop()*(-1))
          elif elem == "^":
               v_etu=s.pop()
               eto=s.pop()
               s.push(eto ** v_etu)
          elif elem == "/":
               zn=s.pop()
               chisl=s.pop()
               s.push(chisl / zn)
     while not s.isEmpty():
          print(s.pop())
          
          
print(rpn("2 2 2 + *"))   #⇒     8
print(rpn("2 2 2 * +"))   #⇒     6
print(rpn("2 3 + 2 ^"))   #⇒    25
print(rpn("8 _ 2 / 3 ^")) #⇒ -64.0
               