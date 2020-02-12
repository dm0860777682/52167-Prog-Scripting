"""
This will generate 10 random numbers (0-100), prints them out then prints out the top three
ref: https://www.w3schools.com/python/module_random.asp
"""
import random
list = []
inNum = 0
output = " "
while inNum != 11:
            num = random.randrange(0,100,1)
            list.append(num)
            list.sort()
            inNum += 1
for x in range(len(list)):
       output = output+","+str(list[x])

result = output.replace(",","",1)
result = result.strip()
print("[",result,"]")
print("[",list[0],",",list[1],",",list[2],"]")
