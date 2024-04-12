
# Python Lab (CS500L)/Week:01/Lab:01/Q:01
# 20099_MANIRUZZAMAN_MD
# Write a Python program that generates a random number between 1 and 100.

import random
print("Guess a number between 1 nad 100.")

##Generte a secret number by random generator
secret = random.randint(1,100)
num_tries = 0

# Ask the user to guess the number
while True:
    guess=int(input("Enter your guess number: "))
    num_tries +=1
    
    #compare the guess and secret
    if guess < secret:
        print("Too low! Guess and try again.")
    elif guess > secret:
        print("Too high! Guess and try again.")
    else:
        print("Congratulations! Your guess is correct. You tried", num_tries, "times")
        break
