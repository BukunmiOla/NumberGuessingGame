#import library
import random

#Declare Variales
guess_power = 1
playing = 1

def difficulty(level):
    
    if level == '1' :
        guess_power = 6
    elif level == '2':
        guess_power = 4
    elif level == '3' :
        guess_power = 3
    else :
        guess_power = int(random.choice("346")) 

    return guess_power

def pick_range(guess_power):
    if guess_power == 6:
        num_range = 10
    elif guess_power == 4:
        num_range = 20
    else:
        num_range = 50

    return num_range

    
print ("Hey! It's good to have you here, This is a number guessing game")

while playing == 1:
    print("Select difficulty level Easy-1, Medium-2, Hard-3 or any other key for a random game")
    level = input()
    guess_power = difficulty(level)
    print ("Okay! you have ", guess_power, "lives in total")
    num_range = pick_range(guess_power)
    while guess_power>0:
        print("Are you ready? ")
        hidden_number = random.randint(1,num_range)
        print ("The hidden number is in the range of 1 to ", num_range)
        guess = int(input("Guess! Guess!! Guess!!!  "))
        print ("Yo! The number is... ",hidden_number)
        if guess == hidden_number:
            print("You got it right!")
            break
        else:
            guess_power-=1
            print ("That was wrong! you have ",guess_power," lives left.")
            try_again = input ("Enter 1 to try again or any other key to quit: ")
            if not try_again == '1':
                exit()




    else:
        print ("Game Over!")
    
    print ("Do you want to play again? ")
    response = input("Enter 1 for yes or any other key for no: ")
    if not response == '1':
        playing = 0