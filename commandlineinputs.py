import sys
def get_user_inputs():
    num1 = ""
    num2 = ""
    while True:
        num1 = input("Enter first Number: ")
        if not num1.isnumeric():
            print("invalid input, must be a number")
        else:
            break
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
    def main():
        print("number 1")
        print("number 2")
        while True:
            first_number = input("first number")
            if first_number.isnumeric():
                print("ok")
                break
    if __name__ == " __main__":
        main()