k = 0
 
with open("textFile.txt", 'r') as f:
    for line in f:
        words = line.split()
        #print(words)
        for i in words:
            for letter in i:
                if(letter=='e'):
                    k=k+1
print(k)