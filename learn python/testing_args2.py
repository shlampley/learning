name = ""
age = ""
hair_color = ""
eye_color = ""
height = ""
weight = ""

def user_input(query, qtype):
    while True:
        # Old way of doing f strings
        user_answer = input("What is your {}".format(query))
        if qtype == "num":
            # Check if the users answer is numeric
            if user_answer.isnumeric():
                break
            
        elif qtype == "alpha":
            if user_answer.isalpha():
                break
            # check if it is alpha

    return user_answer
        
        
def out_put(name, age, hair_color, eye_color, weight):
    # print("hello " + name + " you are " + age + " years old, you have " + hair_color + " hair, and " + eye_color + " eyes," + " you are " + weight + " lbs." )
    print(f"hello {name} you are {age} years old, you have {hair_color} hair, and {eye_color} eyes, you are {weight} lbs." )
    # Lookup python f strings for more information

out_put(age = user_input("Age: ", "num"), hair_color = user_input("Hair color: ", "alpha"), eye_color = user_input("Eye color: ", "alpha"), weight = user_input("Weight: ", "num"), name=user_input("Name: ", "alpha"))