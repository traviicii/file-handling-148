
# Create and write our first file
file = open('new_file.txt', 'w')
file.write('Writing to a file from Python!') # Using the .writ() method to write data to a file
file.close() # this ensures that data gets commited, and keep your computer from harm

# Overwriting a file
file = open('new_file.txt', 'w')
file.write('Overwriting previous data\n')
file.close()

# Add to a file (without overwriting)

file = open('new_file.txt', 'a') # 'a' mode appends where our last entry left off without overwriting
file.write('Adding to my file with "a" mode!\n')
file.close()

# Reading Files
file = open('new_file.txt', 'r') # read a file with 'r' mode
# content = file.read() # return us a large string of the entire text
lines = file.readlines() # returns a list of items defined by new lines
file.close()
# print(content)

#-- with : allows us to open files to a specific code block and automatically closes the file when the code block is exited

with open('new_file.txt', 'r') as file:
    for line in file:
        print(line.strip()) # remove the \n from each line

#----------

#-- Storing data from a list

flowers = ['Wysteria', 'Sun Flowers', 'Orchids', 'Marigolds']
with open('garden.txt', 'w') as file:
    for flower in flowers:
        file.write(flower + '\n')


#-- storing data from a dictionary

clubs = {
    'Driver': 'Cobra',
    'Irons': 'Sirixion',
    'Hybrid': 'Callaway',
    'Putter': 'Ping'
    }

with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f"{club}: {brand}\n")


# Storing data from a nested dictionary
#-- { title: {author: name, genre: name, desc: summary}}

books = {
    'Green Lights': {'Author': 'Matthew McConaughey', 'Genre': "Biography", 'Desc': 'this is a really cool book'},
    'Cloud Atlas': {'Author': 'David Mitchell', 'Genre': 'Sci-Fi', 'Desc': 'I really, love this book!'},
    'Diary of a Wimpy Kid': {'Author': 'Jeff Kiney', 'Genre': 'YAF', 'Desc': 'A tale of a wimpy kid'},
    'Black Flags': {'Author': 'Joby Ray', 'Genre': 'Nonfiction', 'Desc': 'Potentially, this is a story about pirates?'},
    '1984': {'Author': 'George Orwell', 'Genre': 'Fiction', 'Desc': 'Crazy distopyian future stuff'}
}

def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f"{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n")

add_books(books)