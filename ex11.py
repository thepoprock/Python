print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "Scale dave's lameness percentile",
lameness = raw_input()
if int > 100:
    print "no...no...that can't be possible!"

print "So, you're %r old, %r tall and %r heavy... oh and %r percent lame." % (
    age, height, weight, lameness)
