#using arrays in data structures
#Arrays stores data in one data type in a single array
#The data items are enclosed in curly brackets
#An array is mutable (data items stired in the different indices can be be changed as long as they are of the same data type)
#Syntax
#import the array module
#array_name=stated_array.array("data_type", [array])

#Code starts here. Demo with methods 

#importing array liblary
import array as type
#creating the array

#my_array=type.array("i", [23,24,35] )
#my_sec_array=type.array()
#printing 
#print(my_array)
#print(my_array[0:1])
#Append()
'''var=23
var_2=45
var_3= int(input("Enter a numeral value: "))

my_sec_array.append(var)
my_sec_array.append(var_2)
my_sec_array.append(var_3)'''

#insert()
new_array=type.array("u") #character array, unicode
#variables
var3="E"
var4="V"
var5="K"
var5= input("Enter a character value: ")
var6=input("Enter a character value: ")

new_array.insert(1, var3)
new_array.insert(2, var4)
new_array.insert(4, var5)
new_array.insert(5, var6)
print(new_array)
print(new_array[2])

'''newarray2=type.array("f") #float array
newarray2.insert(0,3.13)
print (newarray2)'''


