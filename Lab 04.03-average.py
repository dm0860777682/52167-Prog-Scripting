"""
Write a program(lab04.03-­‐average.py)that keeps reading numbers until the user enters a 0. 
The program    should then print out each of the numbers entered and the average of them.

"""
numInput = 1
list = []
while numInput != 0:
    inputNum = float(input("enter number (0 to quit): "))
    if inputNum != 0:
        list.append(inputNum)
        numInput =1 
    else:
        numInput = 0
        listlen = len(list)
        avr = 1
        for x in list:
            avr += x
        print(avr/listlen) 