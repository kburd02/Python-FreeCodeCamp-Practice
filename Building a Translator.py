
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #if letter.lower(or upper)
             translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
#print out a translation of whatever the user puts in