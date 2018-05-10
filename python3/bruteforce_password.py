#!/usr/bin/python3

import time

print("Please enter a password to test: ")
password  = input()
length = len(password)
print("Starting bruteforce attack on your " + str(length) + " digit password.")
attempts = 0
pwpt = a = [0] * length
start_time = time.time()
end = pow(94, length)

for x in range(0,end):
    for y in range(0, length):
        num = x/pow(94,y)
        pwpt[y] = chr(int(num % 94 + 32))
    #Uncomment the line below to see how it works. Script will be much slower than
    #print "".join(pwpt)
    attempts += 1
    if "".join(pwpt) == password:
        break
        
tempus = time.time() - start_time

print("Successful bruteforce after " +  str(tempus) + " seconds and " + str(attempts) + " attempts")
print("Your password is " + "".join(pwpt))
print("Added the 11% for length guessing, the bruteforce time is " + str(tempus * 1.11) + " seconds")
