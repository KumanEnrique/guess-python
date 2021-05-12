import random

guessesTaken = 0
minNumber = 1
maxNumber = 20

print('hello! what is your name?: ')
username = input()

number = random.randint(minNumber,maxNumber)
print("well, " + username + "iam thinking in a number between " +str(minNumber) + " and " + str(maxNumber) )

while guessesTaken < 6:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    if guess < number:
        print("your guess is too low.")
    if guess > number:
        print("your guess is too high.")
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("good job. "+ username + "you guessed my number in " + guessesTaken + " guesses")
if guess != number:
    number = str(number)
    print("no the number i was thinking of was " + number)