
def add(a,b):
    result = float(a) + float(b)
    print("add: ",result)

def subtract(a,b):
    result = float(a) - float(b)
    print("substract: ", result)

# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

print("First number: ", num1, " Second number: ", num2)
add(num1, num2)
subtract(num1,num2)
