#Ka'Pri Burden
#06/10/2022

#Perform all operations and allow the user to choose what values

#1st get input

num1 = float(input("Enter first number: "))

#operation
op = input("Enter operation to be used: ")
#Python understands it to be a string regardless of the input so use float to convert it


num2 = float(input("Enter second number: "))
#second number

#Check to see the operator

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)

else:
    print( "Invalid operator")
