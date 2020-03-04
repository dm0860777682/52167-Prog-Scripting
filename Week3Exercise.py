<<<<<<< HEAD
print("Loop over String program ")
# Write a program that takes askes a user to input a string  and outputs every seconnd letter in reverse order.
# Referenence: https://www.geeksforgeeks.org/print-without-newline-python/
try:
    #Ask user for input
    UserSentence = input("Please enter a sentence: ")
    senlength = len(UserSentence)
    #Reverse the users input string
    RevUserSen = UserSentence[senlength::-1]
    RevSentence = []
    #Iterate over the user input string and print out every 2nd element
    #### string[start:stop:step size]####
    for x in RevUserSen[0:senlength:2]:
        RevSentence.append(x)
    #printing the list using * and sep operator
    print(*RevSentence, sep = " ")
  
except Exception:
    #This will stop program will not fall over if this user does not enter a integer. 
    print("sorry, somthing went wrong!")
=======
print("Loop over String program ")
# first attempt
# Write a program that takes askes a user to input a string  and outputs every seconnd letter in reverse order.
try:
    #Ask user for input
    UserSentence = input("Enter your Sentence: ")
    senlength = len(UserSentence)
    #Reverse the users input string
    RevUserSen = UserSentence[senlength::-1]
    #Iterate over the user input string and print out every 2nd element
    #### string[start:stop:step size]####
    for x in RevUserSen[0:senlength:2]:
        print(x)
except Exception:
    #This will stop program will not fall over if this user does not enter a integer. 
    print("sorry, somthing went wrong!")
>>>>>>> 57101401e4c6e6b73e53601795af86a45003d7a2
