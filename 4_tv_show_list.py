import re
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

def add_shows(shows):
    clear()
    title = input("What's the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("What is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)

def read_shows(): # Reading shows list and returning the list
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

def remove_show(shows):
    view(shows)
    option = int(input("Choose a number for the show you'd like to remove: "))
    show = shows.pop(option - 1)
    print(f"{show['Title']} was removed!")
    write_show(shows)

def view(shows):
    clear()
    print('Shows List')
    print("---------------")
    for idx, show in enumerate(shows):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")



def main():
    shows_list = read_shows()
    while True:
        
        action = input('''
Options
-----------------------
1 - Add a TV show
2 - Remove a TV show
3 - View List of Shows
4 - Quit
''')
        if action == '1':
            add_shows(shows_list) # funtion to add a show
        elif action == '2':
            remove_show(shows_list) # function to remove a show
        elif action == '3':
            view(shows_list) # View list of shows
        elif action == '4':
            print("Thanks for using this app!")
            break

main()