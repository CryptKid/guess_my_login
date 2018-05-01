#!/usr/bin/python
import time
print "Please enter a password to test:",
password  = raw_input()
lenght = len(password)
print "Starting bruteforce attack on your " + str(lenght) + " digit password"
attempts = 0
pwpt= a = [0] * lenght
start_time = time.time()
for x in range(0,pow(94,lenght)):
    for y in range(0, lenght):
        pwpt[y] = chr(x/pow(94,y) % 94 + 32)
    #Uncomment the line below to see how it works. Script will be much slower than
    #print "".join(pwpt)
    attempts += 1
    if "".join(pwpt) == password:
            break
tempus = (time.time() - start_time)
print("Successful bruteforce after " +  str(tempus) + " seconds and " + str(attempts) + " attempts")
print("Your password is " + "".join(pwpt))
print("Added the 11% for lenght guessing, the bruteforce time is " + str(tempus * 1.11))
