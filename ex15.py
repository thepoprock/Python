#imports arguement
from sys import argv
#defines what the argument is
script, filename = argv
#opens a txt document with the given filename
txt = open(filename)
# prints statement as well as the file
print "Here's your file %r:" % filename
#preforms the read function on the txt document without any parameters, meaning that it will print the document in its entirety.
print txt.read()
#prompts the user to retype the filename (could in theory enter a differnt filename?)
print "Type the filename again:"
#defines file_again as whatever the users puts in
file_again = raw_input("> ")
#opens the provided filename
txt_again = open(file_again)
#prints the given filename without parameters
print txt_again.read()
