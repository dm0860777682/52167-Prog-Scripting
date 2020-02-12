"""
That reads in students until the user enters blank in they students first name. 
The program should then print out all the students entered in a neat way
"""
nameList = []
inNum = 1
while inNum != 0:
    firstName = input("enter firstname (blank to quit): ")
    if firstName == '':
        inNum = 0
    else: 
        inNum = 1
        surName = input("enter surName: ")
        middleName = " "
        name = firstName + middleName + surName
        nameList.append(name)
print("here are the students you entered: ")
for x in nameList:
    print(x)
   
    

