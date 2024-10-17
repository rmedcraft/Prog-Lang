import json

with open("bookstore.json", "r") as file:
    root = json.load(file)

print(root)

# Titles of the books followed by Year
for book in root:
    print(book)
    for child in root[str(book)]:
        print(child) # just prints the keys???

# for i in root["book1"]:
#     print(i)

# Titles of the books followed by all authors

# Total cost of all books

# List of all books year greater than 2003

# Book title and category
