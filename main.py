print("Student Management System")
rollno = dict()
while True:
    print("1" + " Add Student")
    print("2" + " Search Student")
    print("3" + " Delete Student Data")
    print("4" + " Close the program")
    user = input("What action you want to perform ")
    if user == "1":
        student_roll = int(input("Enter Your Roll no.: "))
        rollno[student_roll] = list()
        student_name = input("Enter Your Name: ")
        rollno[student_roll].append(student_name)
        student_mark = int(input("Enter Your mark: "))
        rollno[student_roll].append(student_mark)
        print(rollno)
    elif user == "2":
        roll = int(input("Enter the roll no. "))
        if roll in rollno:
            print(rollno.values())
        else:
            print("Roll Number Doesn't exists")

    elif user == "3":
        roll = int(input("Enter the roll no. "))
        if roll in rollno:
            rollno.pop(roll)
    else:
        exit()
