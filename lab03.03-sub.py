num1 = int(input("Enter first number: "))
num2 = int(input("Enter the number you want to divide by:"))
answer = int(num1 / num2)
remainder = num1%num2
print("{} divided by {} is {} with remainder {} " .format(num1,num2, answer, remainder))