print("String connverter")
# Write a program that takes askes a user to input a string  and outputs every seconnd letter in reverse order.
try:
    #Ask user for input and convert from string to float
    UserSentence = input("Enter your Sentence: ")
    senlength = len(UserSentence)
    print(senlength)
    
    for x in UserSentence[0:senlength:2]:
        print(x)
     
   
except Exception:
    #This will stop program will not fall over if this user does not enter a integer. 
    print("sorry, somthing went wrong!")
