#performing append mode and adding new statemnts to the file.
#Checking how append function works

var_name = open("file1.txt",  "a")

var_name.write("I can't find my pen")
var_name.write("I really miss my previous laptop")
var_name.write("Close the operation")

var_name.close()