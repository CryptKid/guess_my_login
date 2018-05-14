#!/usr/bin/python2

import time
#performing sample attack on 4 digits to find out pc speed
start_time = time.time()
btpin = 0
while btpin != 9999:
	btpin += 1
#Calculating time per digit
time_base = (time.time() - start_time)/10000
#Asking for the number of digits
print "How many digits does your pin have?",
digits_string  = raw_input()
digits = int(digits_string)
#Doing some math to it
after = 9 * pow(10,digits-1)
before = 0
for x in range(1, digits+1):
	before = before + 9 * pow(10,x-1)
percent = float(after) / float(before) * 100
#Telling you the results
print("Before you told me, your pin has " + str(digits) + " digits, I would have needed a maximum of ")
print(before)
print("attempts. I would have needed")
print(str(float(time_base * pow(10, digits))/percent*100))
print("seconds to perform an attack. Now I would only need ")
print (after)
print ("attempts. I can perform them in")
print (str(time_base * pow(10, digits)))
print ("seconds. That's only " + str(percent) + "% of the afford")
