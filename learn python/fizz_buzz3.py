
number = 0
variables = "" 

def fizz_buzz(num, var):
    fizzarray = []
    # doneTODO: Create an empty array outside the loop to store data
    var = variables
    num = number
    while num < 100:
        # Reset var to prevent issues of adding buzz to buzz or buzz to fizzbuz
        var = ""
        #print(num)
        num += 1
        # if num % 3 == 0 and num % 5 == 0:
        #     var = "fizz_buzz"
        #    continue
        # DONE: Depending on which conditions are met set var to either the number of fizz or buzz or both
        if num % 3 == 0:
            var = "fizz"
        if num % 5 == 0:
            var += "buzz"
        # else statement  used in this instance will cause overwrighting of saved fizz data, must use if statement.
        if var == "":
            var = num
        # doneTODO: add var to the end of the array
        fizzarray.append(var)
        # look up storing as list in an array
    return fizzarray
        
def print_array(arr):
    for item in arr:
        print(item)



def out_put(fizzarray):
    # for idx, x in enumerate(fizzarray):
    #     #print(idx, x)
    for ind, x in enumerate(fizzarray):
        if (ind + 1) % 2 == 0:
            print("\t" + str(x))
        else:
            print(x)
        #results.append(fizzarray)
    #print(fizzarray)
        # TODO: if the index is odd no indent
        # TODO: if the index is even indent
    # while i < fizzarray.len():
    #     # instead of x you would use:
    #     fizzarray[i]
    #     i = i + 1

fizzarray = fizz_buzz(number, variables)
# print_array(fizzarray)
out_put(fizzarray)

