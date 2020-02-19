def add(name,id,courseName, grade):
    student = {
        "name": name,
        "Student id" : id,
        "modules": [
            {
                "courseName":courseName,
                "grade": grade
            }
        ]
}
    return student

def dis(list):
    print("View the list")
    if(len(list) == 0):
         print("****** empty list ***********")
       # usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")
       # print("you chose " + usein)
    else:
        for i in list:
            print(i)


list = [] 
usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")       
print("you chose " + usein)
while usein != "q":
    if(usein == "a"):
        print("Add new student")
        name = input("Enter a name:")
        courseName = input("Enter a courseName:")
        id = input("Enter your student id:")
        grade = input("Enter a grade:")
        list.append(add(name,id,courseName,grade))
        usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")
        print("you chose " + usein)
    elif(usein == "v"):
        print("you chose " + usein)
        dis(list)
        usein = input("What would you like to do? \n(a) Add new student \n(v) View students \n(q) Quit\n Type one letter (a/v/q):")
        print("you chose " + usein)

