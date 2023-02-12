print("Welcome to my simple quiz!")

#for input, use function input()
playing = input("Do you want to play? ")

#use .lower() to convert to lowercase
#use .upper() to convert to uppercase

#text = "HeLLo BEE"
#print(text.lower())

#use quit() to quit the program
if playing.lower() != "yes":
    quit()
else:
    if playing.lower() == "yes":
        print("Okay, let's play!")

score = 0

#first quiz question
answer = input("    What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

#second quiz question
answer = input("    What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

#third quiz question
answer = input("    What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

#fourth quiz question
answer = input("    What does RPG stand for? ")
if answer.lower() == "role-playing game":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

#fifth quiz question
answer = input("    What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5 ) * 100) + "%.")

