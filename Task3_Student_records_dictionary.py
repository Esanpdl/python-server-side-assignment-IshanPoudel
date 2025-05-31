#To add a new record to the dictionary list.
def add_record(record):
    name = input("Enter the name of the student: ")
    roll_no = int(input("Enter the roll number: "))
    marks = int(input("Enter the marks secured: "))
    contact_number = int(input("Enter the contact number: "))
    student_dictionary = {"name" : name, "roll" : roll_no, "marks" : marks, "contact" : contact_number}
    record.append(student_dictionary)
    print("Records added successfully.")
    return

#To search record from the dictionary list.
def search_record(record):
    roll_no = int(input("Enter roll number of the student to find:"))
    print("\n\n{:<15}{:<15}{:<15}{:<15} \n".format("Name", "Roll", "Marks", "Contact no."))
    print("*"*55)
    for data in record:
        if data['roll'] == roll_no:
            print("{:<15}{:<15}{:<15}{:<15} \n".format(data['name'], data['roll'], data['marks'], data['contact']))
    return

#To display the complete records from the dictionary list.
def display_record(record):
    print("\n\n{:<15}{:<15}{:<15}{:<15} \n".format("Name", "Roll", "Marks", "Contact no."))
    print("*" * 55)
    for data in record:
        print("{:<15}{:<15}{:<15}{:<15} \n".format(data['name'], data['roll'], data['marks'],data['contact']))
    return

#Startup menu
student_records = []
while True:
    print("\n\nMenu:\n 1.Add Record\n 2.Search Record\n 3.Display Records\n 4.Exit \n")
    choice = int(input("Pick an option between 1,2,3 or 4: "))

    if choice == 1:
        add_record(student_records)
    elif choice == 2:
        search_record(student_records)
    elif choice == 3:
        display_record(student_records)
    elif choice == 4:
        print("Program terminated.")
        break
    else:
        print("\nInvalid option. Choose Again!")




