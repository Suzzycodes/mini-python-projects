#calculator app
start = input("Ready to get started?: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = (input("Pick an operator: "))


def add():
    print(num1+num2)

def sub():
    print(num1-num2)

def mul():
    print(num1*num2)

def div():
    print(num1/num2)


while operator == True:
   continue 

if operator == "+":
    print(add())

elif operator == "-":
    print(sub())

elif operator == "*":
    print(mul())

elif operator == "/":
    print(div())

else:
    print("Invalid operator")












