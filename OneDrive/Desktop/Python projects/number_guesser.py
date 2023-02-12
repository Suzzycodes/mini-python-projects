import random

#get a random number within -6 to 10
#r = random.randrange(-5, 11)
#print(r)
#will possibly include the highest number specified e.g. 11 below
#w = random.randint(-5, 11)
#print(w)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

#generate a number
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
         print("You were above the number!")
    else:
        print("You were below the number!")

print('You got it in', guesses, 'guesses')


# i had an issue getting the correct output and was getting frustrated 
# until I decided to quit the terminal and start over again





