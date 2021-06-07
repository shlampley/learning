

def raise_to_power(base_num, pow_num):
    # place to store results
    result = 1
    for index in range(pow_num):# will loop through the amount of times = to pow_num ex 2 will loop twice and 3 would loop 3 times
        # first time through loop it will * base num * result 
        result = result * base_num
    return result

print(raise_to_power(2, 3))

