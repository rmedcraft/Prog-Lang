import json

with open("Prog-Lang/bookstore.json", "r") as file:
    root = json.load(file)

totalCost = 0

# Titles of the books followed by Year
print("Titles of the books followed by Year")
for book in root:
    print("Title:", root[book]["title"] + ", Year:", root[book]["year"])

    totalCost += float(root[book]["price"])
print()

# Titles of the books followed by all authors
print("Titles of the books followed by all authors")
for book in root:
    print("Title:", root[book]["title"] + ", Author(s):", root[book]["author"])
print()


# Total cost of all books
print("Total cost of all books")
print("Total Cost:", totalCost)
print()

# List of all books year greater than 2003
print("List of all books year greater than 2003")
for book in root:
    if int(root[book]["year"]) > 2003:
        print(root[book]["title"], "was written in", root[book]["year"])
print()

# Book title and category
print("Book title and category")
for book in root:
    print("Title:", root[book]["title"], "Category:", root[book]["category"])
print()


# User enter author name and let the user know if you sell any books from that author, if you do list the book(s)
inp = input("What author do you want to search for? ")
foundAuthor = False

for book in root:
    if inp.lower() == str(root[book]["author"]).lower() or list(root[book]["author"]).count(inp) > 0:
        print(root[book]["title"], "was written by", inp)
        foundAuthor = True

if not foundAuthor:
    print("We couldnt find any books written by", inp)

