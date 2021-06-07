


# i wake Up
# if im hungery
    # i eat breakfast

# i leave the house
# if its cloudy
    # i bring an umbrella
# else    
    # i bring sunglasses

# im at a resturant

# if i want meat
    # i order steak
# else
    # i order pasta
# else
    # order salad

        # basic if statement
is_male = False
is_tall = False

if is_male:
    print("you are male ")
else:
    print("you are not a male ")
    
if is_male or is_tall:
    print("your tall, male, or both")
else:
    print("you are niether male or tall")
if is_male and is_tall:
    print("you are a tall male ")
else:
    print("you must be female or a short male")

if is_male and is_tall:
    print("you are a tall male ")
elif is_male and not (is_tall):
    print("you are a short male")
elif (is_male) and is_tall:
    print("you are a tall female")
elif not (is_male) and not (is_tall):
    print("you are a short female")
else:
    print("not tall or male or both")
