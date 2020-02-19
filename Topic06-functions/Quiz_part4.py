list = []
usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")
print("you chose " + usein)
while usein != "q":
    def add(name,courseName, grade):
        student = {
            "name": name,
            "modules": [
                {
                    "courseName":courseName,
                    "grade": grade
                }
            ]
    }
        list.append(student)
    def dis(list):
        for i in range(len(list)):
            print(list[i])
    if(usein == "a"):
        print("Add new student")
        name = input("Enter a name:")
        courseName = input("Enter a courseName:")
        grade = input("Enter a grade:")
        add(name,courseName,grade)
        usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")
        print("you chose " + usein)
    elif(usein == "v"):
        print("View the list")
        if(len(list) == 0):
            print("****no entries*****")
            usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")
            print("you chose " + usein)
        else:
            print(list)
            usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")
            print("you chose " + usein)
    elif(usein == "q"):
        print("Game over!")
    