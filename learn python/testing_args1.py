
name = ""
age = ""
hair_color = ""
eye_color = ""
height = ""
weight = ""

def user_input(query):
    while True:
        fname = input("What is your {}".format(query))
        return fname

def out_put(name, age, hair_color, eye_color, weight):
    print("hello " + name + " you are " + age + " years old, you have " + hair_color + " hair, and " + eye_color + " eyes," + " you are " + weight + " lbs." )

name = user_input("Name: ")
age = user_input("Age: ")
hair_color = user_input("Hair color: ")
eye_color = user_input("Eye color: ")
weight = user_input("Weight: ")
out_put(name, age, hair_color, eye_color, weight)
