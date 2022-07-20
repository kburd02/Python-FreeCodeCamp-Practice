#classes and objects

class Student:
#initialize...map out the attributes of a student; student data
    def __init__(self, name, major, gpa): #defining what a student is by these categories
    #    def __init__(self, name, major, gpa, is_on_probation): #defining what a student is by these categories
        self.name = name
        self.major = major
        self.gpa = gpa
       # self.is_on_probation = is_on_probation
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False