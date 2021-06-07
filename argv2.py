
import sys

def subtraction(values):
    x = values[0]
    y = values[1]
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Invalid inputs, Must be integers")
    sum=x-y
    print("the subtraction is :" ,sum)

def addition(values):
    x = values[0]
    y = values[1]
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Invalid inputs, Must be integers")
    sum=x+y
    print("the addition is :" ,sum)

    while True:
        opperation = input(addition)
        if opperation in (x, y):
            inputs = main(x, y)
            break


def number_check(x, y):
    while True:
        if not x.isnumeric():
            x = input("number please: ")
        if not y.isnumeric():
            y = input("another number please: ")
        if x.isnumeric() and y.isnumeric():
            break
        else:
            print("invalid input, must be a number")
    results = (x, y)
    return results

def check_commandline_args(val1, val2):
    if not val1.isnumeric():
        print("invalid first input! Must be numeric: ")
    if not val2.isnumeric():
        print("invalid second input! Must be numeric: ")

def main():
    x = sys.argv[1] if len(sys.argv) == 2 or len(sys.argv) == 3 else "none"
    y = sys.argv[2] if len(sys.argv) == 3 else "none"
    check_commandline_args(x, y)
    results = number_check(x, y)
    #addition(results)
    input(addition, subtraction)
    
if __name__ == "__main__":
    main()