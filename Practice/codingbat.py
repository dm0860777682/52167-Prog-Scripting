def missing_char(str, n):
    name = str[:n]+""+str[n+1:]
    return name
#print(missing_char("kitten",1))

def front_back(str):
    if(len(str) <= 1):
        return str
    else:
        front = str[:1]
        back = str[len(str)-1:]
        return back+str[1:len(str)-1]+front
#print(front_back("a"))

def front3(str):
    if(len(str) <=3):
        return str+str+str
    else:
        subStr = str[:3]
        return subStr+subStr+subStr
#print(front3("ab"))

def pos_neg(a, b, negative):
    if((negative == True) and (a < 0 and b < 0)):
        return True
    elif((negative == False) and (a < 0 and b >= 0)):
        return True
    elif((negative == False) and (a < 0 or b >= 0)):
        return True
    elif((negative == False) and (a >= 0 and b < 0)):
        return True
    elif((negative == False) and (a >= 0 or b < 0)):
        return True
    elif((negative == False) and (a < 0 and b < 0)):
        return False
    elif((negative == False) and (a < 0 or b < 0)):
        return False
print(pos_neg(-4,-5, False))
