#06/13/2022
#Ka'Pri Burden


employee_file = open("employees.txt", "r")

#print(employee_file.readable())
#readable checks to see if the file is readable

#print(employee_file.read())
#reads the entire file

#print(employee_file.readline())
#reads the line and moves a cursor to the next one
#print(employee_file.readline())
#moves to the next line until printing out every line

#print(employee_file.readlines())
#prints all of it out as an array
#ISSUE WITH FORT 14

#print(employee_file.readlines()[1])
#prints specific lines

for employee in employee_file.readlines():
    print (employee)
#For each component in the file print it out one by one


#make sure to also close the file
employee_file.close()