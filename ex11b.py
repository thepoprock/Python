print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

running = True 
while running:
    answer = int(raw_input("Scale dave's lameness percentile : "))
    if answer < 101:
        print "okay, that seems accurate."
        running = False 
    elif answer > 100:
        print "no...no...that can't be possible! Please try again!"
else:
        print "...I was getting worried."
        lameness = raw_input()

print "So, you're %r old, %r tall and %r heavy... oh and %r percent lame." % (
    age, height, weight, answer)
