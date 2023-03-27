# Python Tast
# PLP Cohort II-Collaboration -Group-117

# Question one

# Write a python program that will display the number 
# and its square in the following format.

print("Question one")

number = 1
SqrNumber = 0 

print('Number' + '\t\t'+ 'Square')
while number < 7:
    SqrNumber = number**2 
    print(str(number) + '\t\t' +  str(SqrNumber)) 
    number += 1 

# Question two

# Write a Python program that prints the length of a string.
# For example of expected results;
# Input Output Explanation
# "" 0 0 because its empty string
# “Jambo” 5 5 because it has 5 characters
# “Power Learn Project (PLP)” ? ?

print("Question two")

print('Input' + '\t' + 'Output Explanation')

string = input("Enter a string: ")
if string == 0:
    print(string, len(string) , " because its empty string")
else:
    print(string, len(string) , " because it has", len(string), "characters")
# str1 = ""
# str2 = "Jambo"
# str3 = "Power Learn Project (PLP)" 
# print(len(str1) , " because its empty string")
# print(len(str2) , " because it has", len(str2), "characters")
# print(len(str3) , " because it has", len(str3), "characters")

# Question Three

# Write a Python program that does the following:
# Prints the character at index i in the string "Live happily ".
# my_string = "Live happily ".
# If the index is out of range, the program should print "i is out of range"
# If the string is empty, the program should print "Empty String"

print("Question Three")

# find the character at index i in the string "Live happily " 
my_string  = "Live happily "
# result = my_string.index('i')
i = input("Enter character i: ")

if i in my_string:
    print('Character found at index: ',i,'in the string ',my_string)
elif my_string == " ":
    print('The string is empty')
else:
    print("i is out of range")
    
