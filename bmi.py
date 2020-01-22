print("BMI CALCULATER")
# this code will calculate Bmi for any user
# try will catch any non number input
try:
    #Ask user for input and convert from string to float
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    #convert height from grams to Kilograms
    height = height/100
    #calculate the bim calculation
    bim = weight/(height**2)#
    #print the result but format the answer to 2 decimal places
    print("BMI is {:2.2f}.".format(bim))
except Exception:
    #This will stop program will not fall over if this user does not enter a integer. 
    print("sorry, somthing went wrong!")
