
def add(x, y):
     return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

    #user input function
def get_user_input():
    num1 = ""
    num2 = ""
    #number check
    while True:
        num1 = input("Enter first Number: ")
        if not num1.isnumeric():
            print("invalid input, must be a number")
        else:
            break
     #number check   
    while True:
        num2 = input("Enter second Number: ")
        if not num2.isnumeric():
            print("invalid input, must be a number")
        else:
            break
    #inputs floated
    num1 = float(num1)
    num2 = float(num2)
    #user inputs
    inputs = []
    inputs.append(num1)
    inputs.append(num2)
    return inputs

def do_math(inputs, opperation):
    num1 = inputs[0]
    num2 = inputs[1]
    if opperation == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif opperation == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif opperation == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif opperation == "4":
        print(num1, "/", num2, "=", divide(num1, num2))

def main():

    # Print out initial instructions
    print("select opperation. ")
    print("1.Add ")
    print("2.Subtract ")
    print("3.Multiply ")
    print("4.Divide ")

    # begin loop for user input
    while True:
        opperation = input("enter operation: ")
        if opperation in ("1", "2", "3", "4"):
            inputs = get_user_input()
            do_math(inputs, opperation)
            break 
        else:
            print("invalid input")

#randomstring = "this is a string"
#if randomstring.isnumeric():
#  do stuff
#else:
#   print("invalid input, your opperation must be a number")

if __name__ == '__main__':
    main()