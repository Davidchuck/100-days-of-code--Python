#Combining read, write and apend funstions

var_name = open("statements.txt", "w")
var_name.write("The teacher wants us to do this on our own\n")
var_name.write("this is statment 2\n")
var_name.write("This is the last line here")

var_name.close()

file_read=open("statements.txt", "r")
print(file_read.read())


var_name = open("statements.txt",  "a")
var_name.write("This is an append statment")
var_name.write("This is final line of this append")

var_name.close()

file_add=open("statements.txt", "r")
for i in var_name: 
    #print(i)
    print(file_add.read())

