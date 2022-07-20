lucky_numbers = [4, 8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

#extenf function- append a litst to another list
friends.extend(lucky_numbers)

print(friends)

#add individual elements
friends.append("Creed")
print(friends)

#insert- two parameters 1 tells you position and then the element that you want to add
friends.insert(1,"Kelly")
print(friends)

#remoce-searches and removes a variable in the list
friends.remove("Kelly")
print(friends)

#clear- resets the entire list within the variable
#friends.clear()
#to debug
print(friends)

#pop- pops an elemnt off

friends.pop()
print(friends)

# tells the index of where Kevin is
print(friends.index("Kevin"))

#count- tells how many times it appears in
print(friends.count("Jim"))

#sort- ascending order
#with alphabets, alphabetical order
#ERROR
#friends.sort()
#print(friends)

# have to unappend it

lucky_numbers.sort()
print(lucky_numbers)

#reverse- reverses the list order

print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

#copy copies data in the lists

friends2 = friends.copy()
print(friends2)