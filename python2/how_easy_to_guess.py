#!/usr/bin/python2
print "How many digits does your pin have?",
digits_string  = raw_input()
digits = int(digits_string)
after = 9 * pow(10,digits-1)
before = 0
for x in range(1, digits+1):
	before = before + 9 * pow(10,x-1)
percent = float(after) / float(before) * 100
print "Before you told me, your pin has " + str(digits) + " digits, I would have needed a maximum of "
print before
print "attempts. Now I do only need up to "
print after
print "attempts. That's only " + str(percent) + "% of the afford"
