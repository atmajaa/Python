#Printing data
message = "Hello World"
print(message)
#Printing the first character
print(message[0])
#Starting from zero till except the fifth char
print(message[0:5])
#Starting from 6th till the last character
print(message[6:])
#Upper and Lower Case
print(message.lower())
print(message.upper())
#Does not make change to the original variable
print(message)
#Count the number of character present in string
print(message.count('o'))
#Find a word or character
print(message.find("l"))
#Replacing a word
print(message.replace("Hello","Meow"))
#Concatinate Strings
name = "Rohan"
mood = "Happy"
print(name + " is " + mood)
#For printing on next line
new_message = """This is an example
for printing
on new line"""
print(new_message)
#To access methods and attributes associated to a particular variable
print(dir(name))