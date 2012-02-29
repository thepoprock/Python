def rage_factor(annoyance, tiredness):
    print "Your level of annoyance is %d." % annoyance
    print "You are %d TIMES above the normal tiredness level." % tiredness
    print "You're probably really tired."
    print "It would actually make sense to get a blanket."
    print "and a pillow...."
    print "A bed too... yeah that wouldn't hurt."

print "Blaaahblaaah, provided values:"
rage_factor(50,50)

print "using scripted values:"
annoyance = 99
tiredness = 99

rage_factor(annoyance, tiredness)

print "Let's do some math:"
rage_factor(44 + 30, 40 + 23) 


print "let's mix the last two!"
rage_factor(annoyance + 900, tiredness + 340)

print "Let's try some user input!!"

annoyance = int(raw_input("Scale your annoyance numerically:"))
tiredness = int(raw_input("How about your level of tiredness?"))  
print "you are %d annoyed and %d tired." % (annoyance, tiredness)
print "this means that your rage factor is %d." % (annoyance + tiredness)

