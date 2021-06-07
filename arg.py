
import sys
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_datatypes.asp

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
    addition(results)
    
if __name__ == "__main__":
    main()



# Main loop containing logic for:
# check if the input from command line arguments is there
# If it is : 
    # Break the loop
# If it isnt:
    # Ask the user for input of X and Y
    # Break The loop

# outside the loop after the loop:
# add the two values and print it out to console
# (x,y) if the value is none we ask them for input 
# while True:
 #   y = ""
  #  if not y:
   #     print("empty string try again")
    #else:
     #   print("not empty")

# if the value is anything other then none we can typecast it
# Stretch goal: research try catch and wrap the typecast in it to catch errors and output feedback to the user.


