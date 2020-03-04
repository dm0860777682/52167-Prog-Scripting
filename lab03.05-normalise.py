import random
num1 = input("Enter the string: ")
#num = random.randint(num1,num2)
num2 = num1.strip().lower()
len1 = len(num1)
len2 = len(num2)
print("The String normalised is : {} " .format(num2))
print("we reduced the input string for {} to {} chartacters" .format(len1,len2))