print("Loop over String program ")
# Write a program that takes askes a user to input a string  and outputs every seconnd letter in reverse order.
# Referenence: https://www.geeksforgeeks.org/print-without-newline-python/, https://www.w3schools.com/python/python_howto_reverse_string.asp
try:
    #Ask user for input
    UserSentence = input("Please enter a sentence: ")
    # Get the lenght of the sentence
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
    #This will catch the excecption. The program will not fall over if this user does not enter string values. 
    print("sorry, somthing went wrong!")
