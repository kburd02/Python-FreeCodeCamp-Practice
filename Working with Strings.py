#06/7/2022

#creating a string variable

#print("Learn Python Youtube freeCodeCamp\nAcademy")
#changes to a variable string
phrase= "Learn Python Youtube freeCodeCamp Academy"
#\n enters a new line
#\" would include a quotation mark ESCAPE CHARACTER... render it literally rather than ending the actual script

#concatentaion is appending another string onto anoter one

#print(phrase + " is cool")

#including a function

print(phrase.upper())
#changes it all to uppercase

#checks to see a true or false value
print(phrase.isupper())


#combines the two line# combine
print(phrase.upper().isupper())


#to check the length and amount in the variable

print(len(phrase))

#indexing the characters
#the first character would be 0
print(phrase[0])

print(phrase.index("G"))
print(phrase.index("Academy"))

#replace uses two values, 1st what to replace and then what with

print(phrase.replace("Learn Python Youtube freeCodeCamp","Elephant"))


