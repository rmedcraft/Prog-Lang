import xml.etree.ElementTree as ET

tree = ET.parse("./bookstore.xml")
root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

# Titles of the books followed by Year

totalCost = 0

print("Titles of the books followed by Year")
for book in root:
    for child in book:
        if(child.tag == "title"):
            print("Title: ", child.text, end=", ")
        if(child.tag == "year"):
            print("Year: ", child.text)
        

        if(child.tag == "price"):
            totalCost += float(child.text)
print()

# Titles of the books followed by all authors
print("Titles of the books followed by all authors")
for book in root:
    for child in book:
        if(child.tag == "title"):
            print("Title: ", child.text, end=", ")
        if(child.tag == "author"):
            print("Author: ", child.text)
print()

# Total cost of all books
print("Total Cost: ", totalCost)
print()

# List of all books year greater than 2003
print("List of all books year greater than 2003")
for book in root:
    for child in book:
        if(child.tag == "year" and int(child.text) > 2003):
            print("Year: ", child.text)
print()

# Book title and category
print("Book title and category: ")
for book in root:
    for child in book:
        if(child.tag == "title"):
            print("Title: ", child.text, "Category: ", list(book.attrib.values())[0])

# User enter author name and let the user know if you sell any books from that author, if you do list the book(s)
inp = input("What author do you want to search for? ")
title = ""
foundAuthor = False

for book in root:
    for child in book:
        if(child.tag == "title"):
            title = child.text
        if(child.tag == "author" and child.text.lower() == inp.lower()):
            foundAuthor = True
            for child in book:
                if(child.tag == "title"):
                    print(child.text, "was written by", inp) 
            break

if not foundAuthor:
    print("We werent able to find any books written by", inp)
