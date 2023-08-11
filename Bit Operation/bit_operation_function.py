#using python's built-in function
#DecimaltoBinary()

#define the function
def DecimalToBinary(n):

#declaring retun for the function
 
 return("{0:b}". format(int(n)))

#calling the function, the number in the function is the decimal number to convert to binary
n=DecimalToBinary(2)

#printing the bit result
print(n)

#method 2
#using the quick ninja methon, bin() function

n=bin(255) #here 255 is the number to concert to binary
print(n) #result prefixes with 0b.
