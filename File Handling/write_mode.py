#second part of file handling lesson
#Writing using python 

#Method 1
var_name=open("file1.txt", "W")

#Writing operation starts here
var_name.write("Hello World")
var_name.write("My name is Dave")
var_name.write("This is the third statement")
var_name.write("Today is Monday")
var_name.write("I check emails everyday")

var_name.close() #closes the file for process of writigng
