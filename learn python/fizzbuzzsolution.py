#############################################################
# Author: Austin Benitez
# Date: 5/22/21
# Assignment: Fizz Buzz
# Description: 
# The rules: Count to 100*
# Every Multiple of 3 is replaced with Fizz
# Every multiple of 5 is replaced with Buzz
# Every multiple of both is replaced with FizzBuzz
# Stretch: every other output is indented
#############################################################\

"""
Given an array stagger print the array offset by a tab for every odd index
"""
def array_stagger_print(array):
    for idx,item in enumerate(array):
        if (idx + 1) % 2 == 0:
            # Here we use f string to format the variable with a tab before it
            print (f"\t{item}")
        else:
            print(item)
"""
Given an array print every item
"""
def array_print(array):
    for item in array:
        print(item)

# Logic for the creation of an array of fizzbuzz format
def fizz_buzz_logic(x):
    temp = ""
    if x % 3 == 0:
        temp = "fizz"
    if x % 5 == 0:
        temp += "buzz"
    if temp == "":
        temp = x
    return temp

def fizz_buzz():
    # Here we use list comprehension to tell it to run our logic function for every number between 1-100
    # and add that value to The fizzybuzzy array, in this example we are calling a function 
    # for readability but we could use in-line logic for the list comprehension:
    # fizzybuzzy = ["fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else "fizzbuzz" if x % 5 == 0 and x % 3 == 0 else x for x in range(1,100)]
    fizzybuzzy = [fizz_buzz_logic(num) for num in range(1, 100)]
    return fizzybuzzy

def main():
    # We call fizz buzz and pass the returned value into the fizzybuzzy array
    fizzybuzzy = fizz_buzz()
    # We call the original print function
    print("Not Formatted:\n")
    print("========================\n")
    array_print(fizzybuzzy)
    print("========================\n")

    # We call the alternating print function
    print("Staggered Output:\n")
    print("========================\n")
    array_stagger_print(fizzybuzzy)
    print("========================\n")

if __name__ == "__main__":
   main()