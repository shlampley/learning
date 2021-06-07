number = 0
def fizz_buzz(num):
    num = number
    while num < 100:
        #print(num)
        num += 1
        if num % 3 == 0 and num % 5 == 0:
            print("fizz_buzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz")
        else:
            print("\t" + str(num))
fizz_buzz(number)



