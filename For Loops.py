#Ka'Pri Burden
#06-10-2022

for letter in "Learn Python Youtube freeCodeCamp Academy":
    print(letter)
#Variable changes for each iteration of the loop

    #Why not have to set letter to be understood

#array example
friends= ["Jim", "Karen", "Kevin"]

#to find the length in frineds: len(friends)
for friend in friends:
    print(friend)
    #can rename friend for whatever you's like just use the same name when calling it


#looping through a series of numbers

for index in range(10):
    print(index)
    #doesnt brint out 10 ,0-10

# can do for specifics

for index in range(3,10):
    print(index)

for index in range(len(friends)):
    print(friends[index]) #for specifics

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")