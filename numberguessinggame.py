import random
list1 = [1,2,3,4,5,6,7,8,9,10]
number = (random.choice(list1))
lives = 5
print("Number Guessing Game V1")
guess = input("Enter your number :- ")
if guess not < or >  number:
    print("Try something else", guess )
    lives = lives - 1
    print("Your Lives Left :- ", lives )
if guess == number:
    print("Congratulations! You have guessed the number correctly!")
    print("The number was :- ", number )
    print("Number of lives left :- ", lives )
if lives == 0:
    print("Oh no! You ran out of lives , You Lost!")
    print("The number was :-", number )
    print("Try again maybe")

