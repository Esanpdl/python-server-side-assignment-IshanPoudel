import csv  #Importing csv module

#Initializing variables
total_marks = 0.0
students_count = 0

#Open csv file in read mode to retrieve data from the file.
with open("studentmarks.csv", "r") as file:
    data = csv.reader(file)

    #Displaying the data within the file and adding marks at the same time.
    print("Student Marks: \n")
    for value in data:
        print(f"Roll_no: {value[0]}   Name: {value[1]}    Marks: {(value[2])} \n")
        total_marks += float(value[2])
        students_count += 1

#Average marks calculation
Average_marks = total_marks / students_count
print("The average marks of the students is: ", Average_marks)

