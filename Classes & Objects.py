#can create our own data types

#student.py

# class Student:
# #initialize...map out the attributes of a student; student data
#     def __init__(self, name, major, gpa, is_on_probation): #defining what a student is by these categories
#         self.name = name #self.name is an attribute of student but name is a value tha tis stroed to this attribute
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation


from Student import Student

#creating an object which is just an instance of the class
student1 = Student("Jim","Business", 3.1, False)
student2 = Student("Pam","Art", 2.5, True)
#these are getting passed into the finction and being stored


#student1 is an object

print(student1.gpa)
#can access each object with student1.(options)

