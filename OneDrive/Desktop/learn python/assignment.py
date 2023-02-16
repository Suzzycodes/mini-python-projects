''' #countdown function for positive numbers
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

#countup function for negative numbers
def countup(n):
    if n >= 0:
        print('blastoff!')
    else:
        print(n)
        countup(n+1)
    
number = int(input('Pick a number: ' ))
countup(number) '''

milk = "skimmed milk"
food = "oats" + milk
print(food)



