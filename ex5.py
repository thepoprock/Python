name = 'Patrick A. Roth'
age = 22 # also not a lie
height_inch = 68 # inches
height_cm = height_inch * 2.54 
weight_lbs = 165 # lbs
weight_kilos = weight_lbs * .45359237
eyes = 'Blue'
teeth = 'White' #ish
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches or %d centimeters tall." % (height_inch, height_cm)
print "He's %d pounds or %d kilos heavy." % (weight_lbs, weight_kilos)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#whatever shaw
print "If I add %d, %d, and %d, I get %d." % (
    age, height_inch, weight_lbs, age + height_inch + weight_lbs)
