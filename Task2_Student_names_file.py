student_names = []
n = int(input("Enter the number of names you want to add in the list: "))

#Names input in the student_names list
for i in range(n):
    name = input("Enter name: ")
    student_names.append(name)

#The student_names list written to a file.
with open("students.txt", "w") as f:
    f.write("Student Names:\n")
    for name in student_names:
        f.write(f"{name}\n")

#The student_names displayed after retrival from the file.
print("\nThe data stored in the file are: ")
with open("students.txt", "r") as f:
    print(f.read())