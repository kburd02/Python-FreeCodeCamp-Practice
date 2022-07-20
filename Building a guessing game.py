# specify a secret word then the user will interact to the program and guess until they get the secret work right

secret_word=  "giraffe"

#storing the guesses made by the user

guess = ""

#Setting a limit to how many times the user has guessed

guess_count = 0
#initially there aren't any guesses


#how many times the user can guess the word

guess_limit = 3

#boolean to check if out of guesses
out_of_guesses = False


#Can there be a way to separate the guesses so that it won't be all cluttered

#prompt the secret word and if wrong then go until they get it right
#Attempt: guess= (input("Please input your guess: "))
# while guess != "giraffe":
#     print ("Sorry, wrong answer. Try again!")
#
# print("Correct! The secret word is 'giraffe'")

while guess != secret_word and not (out_of_guesses):
    #add another condition...if out of guesses, break out using the not out of guesses keep looping

    #check to see if the user has more guesses

    if guess_count < guess_limit:
        #haven't guessed the total amount fo guessses
        guess = input("Enter guess: ")
    #improve to include script for wrong answer
    #want to increment the guess_count everytime you go througt the while loop
        guess_count += 1
    else:
        out_of_guesses= True

#creates aanother if statement because you'll need another else condition
if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("You win!")

#improve code to see if you can play again