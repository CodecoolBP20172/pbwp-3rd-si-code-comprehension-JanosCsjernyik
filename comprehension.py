#  The program gets a random number (1<=n<20), the user have to guess it in 5 tries. The program helps you by saying
# if it is higher or lower then tha random number.

import random  # importing random function

guessesTaken = 0  # assign 0 to guessesTaken varriable

print('Hello! What is your name?')  # printing to terminal the argument
myName = input()  # assign user's input to myName varriable

number = random.randint(1, 20)  # assign a random intiger (1<=intiger<20) to number varriable with randinit function
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # printing to terminal: the argument
# + the user's name, in context

while guessesTaken < 6:  # creating a while loop: goes until guessesTaken=5
    print('Take a guess.')  # printing to terminal the argument
    guess = input()  # assign user's input to guess varriable
    guess = int(guess)  # transform guess varriable to intiger with int() function

    guessesTaken += 1  # adding +1 to guessessTaken variiable

    if guess < number:  # using if keyword to compare guess and number varriables
        print('Your guess is too low.')  # if number is greater than guess varriable, it prits out the argument

    if guess > number:  # using if keyword to compare guess and number varriables
        print('Your guess is too high.')  # if guess is greater than number varriable, it prits out the argument

    if guess == number:  # using if keyword to compare guess and number varriables
        break  # if guess is equal to number varriable it breaks out the while loop

if guess == number:  # using if keyword to compare guess and number varriables
    guessesTaken = str(guessesTaken)  # transform guessesTaken to string with str() function
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # printing out the
    # argument + users's name+user's try number in context, if the user guesssed the number correctly

if guess != number:  # using if keyword to compare guess and number varriables
    number = str(number)  # transform number to string with str() functiion
    print('Nope. The number I was thinking of was ' + number)  # if tha last guess of user is incorrect, it prints out
    # the argument + the randomly generated number in context
