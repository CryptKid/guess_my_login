#!/usr/bin/python2
import time
print "Please enter a pin to test:",
pin_string  = raw_input()
pin = int(pin_string)
print "Starting bruteforce attack"
attempts = 0
start_time = time.time()
btpin = 0
while btpin != pin:
	btpin += 1
	attempts += 1
print("Successful bruteforce after %s seconds " % (time.time() - start_time) + "and " + str(attempts) + " attempts")
print("Your pin ist " + str(btpin))
