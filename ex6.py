x = "There are %d types of people." % 10 # assigns integer 10 to variable 'x'
binary = "binary" #defines binary
do_not = "don't" # defines phrase do_not as don't
y = "Those who know %s and those who %s." % (binary, do_not) #impliments variables from lines 2-3 for the value of 'y'

print x # prints value x
print y # prints value y

print "I said: %r." % y # prints the string name and value for variable 'y'
print "I also said: '%s'." % y # prints the whole string as well as value for variable 'y'

hilarious = False # value/variable
joke_evaluation = "Isn't that joke so funny?! %r" #value/variable

print joke_evaluation % hilarious #print requested value

w = "this is the left side of..." #print..
e = "a string with a right side." #print..

print w + e #print value for variable 'w' then 'e'
