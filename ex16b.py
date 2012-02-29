from sys import argv

script, filename = argv

print "We're going to add to %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input ("?")

print "Opening the file..."
target = open(filename, 'w')

print "Enter the notes you would like to add to %r." % filename

line1 = raw_input("line 1: ")

print "Okay, the notes have been added to %r." % filename
target.write(line1)
target.write("\n")

prompt = '---->'
user_input = raw_input("Are you finished adding notes? \n('yes' to end, otherwise enter additional notes to continue)\n")
while user_input.lower() != 'yes':
    target.write(user_input + "\n")
    user_input = (raw_input("Add notes or type yes to quit \n"))
    
print "And finally, we close it."
target.close()
