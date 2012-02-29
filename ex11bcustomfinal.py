print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#typical pattern (conditional = initial_value,
                                  #while conitional (==) true (or <, >, <=,>=)    

lameness = int(raw_input("How lame are you?")) # things that are above others come before.
max_lameness = 100
while lameness > max_lameness:
    lameness = int(raw_input("try again")) 

print "okay. That seems to be accurate." #after control statements, such as while, leave a blank to indicate endingn point
                                        #things that are below others come after.     
print "So, you're %r old, %r tall and %r heavy... oh and %r percent lame." % (
    age, height, weight, lameness)
