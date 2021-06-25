#define a  function

def my_function():
    print("hello from a function")


#calling  A FUNCTION 

my_function()

# to open a file in python
f=open("./class 98/test.txt")

# read the file and print it on console
f.read()

#by default file open in read mode (r)
open ("./class 98/test.txt",'r')

#file is an object in python which has several function define on them 
#read() function define on file 
# "\n"  represents the enter or return key (goes to a new line)
#readlines() is defined on file object which split the line in the file and stores it in line by line as a list 
#we can print these lines by calling a for loop on the list 
f=open("./class 98/test.txt")
fileLines=f.readlines()
for line in fileLines:
    print(line)

#every thing in python is an object
#split function  uses white space by default
introString="My Name Is Arijeet Diwan And I am 15 year old"
words=introString.split()
print(words)

phrases=introString.split(",")
print(phrases)


