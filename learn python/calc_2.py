num1 = float(input("Enter First Number: "))
op = input("Enter Opperator: ")
num2 = float(input("Enter Second Number: "))
        # basic if  and elif satements for calc
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid opperator")
