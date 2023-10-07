#This is a demonstration on how to crear stacj form a module
#The modul being used is called, deque
#the modules also hold methods sued to get about  
#imports
from collections import deque

mystack=deque()
#appending function
mystack.append(8)
mystack.append(16)
mystack.append(23)
mystack.append(15)
mystack.append(8)

print(mystack.isEmpty())
print(mystack.getSize())
