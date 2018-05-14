#!/usr/bin/python3

import time
#asking for amount of digits
print("How many digits does your pin have?")
digits_string  = input()
start_time = time.time()
#performing a sample attack on a 4 digits pin to test pc speed
btpin = 0
while btpin != 9999:
	btpin += 1
#calculating time per digit
time_base = (time.time() - start_time)/10000
#adding some math
digits = int(digits_string)
after = 9 * pow(10,digits-1)
before = 0
for x in range(1, digits+1):
	before = before + 9 * pow(10,x-1)
percent = float(after) / float(before) * 100
#tell you the results
print("Before you told me, your pin has " + str(digits) + " digits, I would have needed a maximum of ")
print(before)
print("attempts. I would have needed")
print(str(float(time_base * pow(10, digits))/percent*100))
print("seconds to perform an attack. Now I would only need ")
print (after)
print ("attempts. I can perform them in")
print (str(time_base * pow(10, digits)))
print ("seconds. That's only " + str(percent) + "% of the afford")
