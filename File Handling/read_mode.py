
var_name=open("file1.txt", "r")
for each in var_name:
    print(each)
    #print(var_name)

    #read mode second demo
file_read=open("file1.txt", "r")
print(file_read.read())

with open("file1.txt") as file_read:
    text=file_read.read()
    print(text)

#performing split operation on a file
with open("file1.txt", "r") as data:
    data_1=data.readlines()
    for line in data_1:
        var=line.split()
        print(var)

