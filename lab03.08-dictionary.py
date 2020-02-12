currentBook =	{
  "title": "Harry potter eats his dinner",
  "author": "Just Kidding Rowling",
  "price": 12
}
print(currentBook)
print(currentBook["author"])
currentBook["ISBN"] = "1233345"
print("The current book has these values:")
for values in currentBook.values(): print(" =>{}" .format(values))

#print("The Random Fruit : {} " .format(fruits))
#print("we reduced the input string for {} to {} chartacters" .format(len1,len2))