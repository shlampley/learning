number = 1


def fizz_buzz(num):
    number = num
    while num < 101:
        print(num)
        num += 1
        if num % 3:
            print("fizz")
        elif num % 5:
            print("buzz")
        elif num % 3 == number % 5:
            print("fizzbuzz")
        

fizz_buzz(number)
