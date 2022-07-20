


try:
    #value= 10/0
    answer = 10/0
    #doesn't work
    number = int(input("Enter a number: "))
#converts it to an integer
    print(number)

except ZeroDivisionError as err: #can except specidic errors
    print(err) #sets Zero deividion error messfe as error
except ValueError:
    print("Invalid Input")

#Try/except