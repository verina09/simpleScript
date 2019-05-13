
def add(a,b):
    result = float(a) + float(b)
    print("add: ",result)

def subtract(a,b):
    result = float(a) - float(b)
    print("substract: ", result)

# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

print("num1: ", num1, " num2: ", num2)
add(num1, num2)
subtract(num1,num2)
