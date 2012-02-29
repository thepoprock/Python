from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying %s to %s" % (from_file, to_file)

#combination
input = open(from_file)
indata = input.read(from_file)

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Completed."

output.close()
input.close()
