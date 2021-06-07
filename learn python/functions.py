

        # funtions are a collection of code to perform a task so it can then be called
        # test function

def user_inputs(name, age):
        name = input("Name: ") # my add on
        age = input("Age: ")
        return name, age

        # define paremeter inside (as, many, as, you, want):

def say_hi(name, age):
    print("hello " + name + " you are " + age)
        # flow of program top to bottom
def main():
    name = user_inputs([0])
    age = user_inputs([1])
print("Top")
say_hi(name, age)
print("Bottom")

if __name__ == '__main__':
    main()
