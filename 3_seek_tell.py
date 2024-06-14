# Tell and Seek

with open('new_file.txt', 'a+') as file:
    file.write('Adding something totally new\n') # writing with 'a+'
    print(file.tell())
    file.seek(54)
    content = file.read()
    print(content)