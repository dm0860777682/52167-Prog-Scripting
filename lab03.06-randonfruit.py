import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear', 'Potato')

num = random.randint(0,len(fruits)-1)
#num2 = num1.strip().lower()
#len1 = len(num1)
#len2 = len(num2)
fruits = fruits[num]
print("The Random Fruit : {} " .format(fruits))
#print("we reduced the input string for {} to {} chartacters" .format(len1,len2))