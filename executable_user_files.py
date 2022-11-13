filename = input("what is the filename?")
content = input("Enter the contents:")

with open (filename, 'w') as file:
    file.write(content)

open_file = input("would you like to open file?")
if open_file in ['y', 'n']:
    if open_file == 'y':
        with open (filename, 'r') as file:
            print(file.read())

# this code lets you create a new file and content from user inputs and lets you read the content in your terminal
