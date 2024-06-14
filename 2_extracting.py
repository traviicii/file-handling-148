from helper import d
# Extracting list data

flowers = []
with open('garden.txt', 'r') as file:
    for line in file:
        flowers.append(line.strip()) # remove default whitespace, \t, \n

print(flowers)

d()

# Extract dictionary data

golf_clubs = {}

with open('golf_bag.txt', 'r') as file:
    for line in file:
        club, brand = line.strip().split(': ')
        # print(club)
        golf_clubs[club] = brand

print(golf_clubs)

d()

# Extracting more dense dictionary data

def read_books():
    books = {}
    with open('books.txt', 'r') as file:
        for line in file:
            title, author, genre, desc = line.strip().split('-:-')
            books[title] = {'Author': author, 'Genre': genre, 'Desc': desc}
    return books

def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")


# Utilize our read and write functions to extract data, change the data, overwrite previous data

def edit_books():
    books = read_books() # Grabs all the books from our local file
    title = input("What book would you like to change? ")
    if title in books:
        desc = input("Give a new description: ")
        books[title]['Desc'] = desc

    add_books(books)

edit_books()