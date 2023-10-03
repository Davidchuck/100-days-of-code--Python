#linear data structure that stores information on a linear way
#uses concept of LIFO
#Two methods are used to uild a stack
#1 being lists
#2 being arrays
#to access data inside a stack one must use a method called pop

#A simple stack demo
stack = [] #empty list
# We will add data using append function
#Pushing data inside a stack
stack.append(5)
stack.append(6)
stack.append(7)
stack.append(8)
#print(stack)
#print("Stack after pushing 5 and 6 is ",end="")

#Accessing data inside a stack
#Uses the pop method
print(stack.pop())
print(stack)
