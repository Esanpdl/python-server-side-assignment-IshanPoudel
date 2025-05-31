#Defining a class named Student
class Student:
    # Constructor to initialize attributes
    def __init__(self):
        self.name = ""
        self.roll = None
        self.marks = 0.0

    #method to input detail from the user.
    def input_details(self):
        self.name=(input("Enter name:"))
        self.roll=int(input("Enter roll number:"))
        self.marks=float(input("Enter marks:"))

    #Method to display the entered details.
    def display_details(self):
        print("Entered details are:\n")
        print(f" Name:{self.name}\n Roll Number:{self.roll}\n Marks:{self.marks}")

#Creating instance of the Student class
student1=Student()

#Calling the methods
student1.input_details()
student1.display_details()