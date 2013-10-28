# this allows for use of the argv command, so we can write the txt filename
from sys import argv

# this specifies the arguments that python will ask for initially
script, filename = argv

# this defines a variable named txt which is assigned to the user-specified filename
txt = open(filename)

# this prints a line that informs users about the name of the requested file
print "Here's your file %r:" % filename

# this calls a function on the txt variable, which is essentially calling 
# the read function on the requested file itself. It will print out the contents
# of the text file.
print txt.read()
txt.close()

# this will print a prompt to ask the user to write the file again.
print "Type the filename again:"

# this assigns the user input to the new file_again variable
file_again = raw_input("> ")

# this takes the user input filename and assigns the file contents to a new variable
txt_again = open(file_again)

# this is identical to line 16. .read() function is called on new txt variable
print txt_again.read()
txt_again.close()