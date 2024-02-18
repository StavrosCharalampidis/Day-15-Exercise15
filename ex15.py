# import from sys the argv module
from sys import argv

# Those args is input from the terminal
script, fileName = argv

# open the txt with the name text
text = open(fileName)

# Printing the text by the method read 
print(f'The File is {fileName}:\n{text.read()} \n')

# Print something for user know 
print("Type the file name: ")

# The Variable fileName2 store a string
fileName2 = input('>')

# open the txt with the name textAgain
textAgain = open(fileName2)

# Printing the textAgain by the method read 
print(f'{textAgain.read()}') 