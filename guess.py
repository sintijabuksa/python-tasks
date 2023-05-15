# import random module; used to perform actions randomly, for example:
# to get a random num, select a random elem. from a list, shuffle elem randomly, etc.
import random
# prints greeting message and asks user to provide his name
print("Hello, there! Are you ready to play guessing game? Please, type in your name: ")
# prompt the user to provide his name and store it in a variable named "name"
name = input()
# generate random number between 1 to 7 and store it in a variable named "num"
num = random.randint(1, 7)
# guess will store the guesses
guess = 0

# while loop is gonna continus till the user guess is right
while guess != num:
    # promt the user to enter the quess
    # input function will return the string that is entered
    # int will take that string and convert it into int and gonna store result into guess
    guess = int(input("Try to guess a number between 1 and 7: "))
    # if the guess is lower than the number user needs to guess
    if (guess < num):
        # prints hint to guess higher number
        print("Guess higher number!")
        # otherwise if the guess is higher than the number
    elif (guess > num):
        # prints hint to guess lower number
        print("Guess lower number!")
        # otherwise the only possibility is that the number is correct
    else:
        # prints out the message when the user guesses the correct number
        print("Congrats, " + name + "! You have guessed the right number.")


