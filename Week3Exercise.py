print("Loop over String program ")
# Write a program that takes askes a user to input a string  and outputs every seconnd letter in reverse order.
try:
    #Ask user for input
    UserSentence = input("Enter your Sentence: ")
    senlength = len(UserSentence)
    RevUserSen = UserSentence[senlength::-1]
    #Iterate over the user input string and print out every 2nd element
    #### string[start:stop:step size]####
    for x in RevUserSen[0:senlength:2]:
        print(x)
except Exception:
    #This will stop program will not fall over if this user does not enter a integer. 
    print("sorry, somthing went wrong!")
