

def translate(phrase):
    # making a place to store returned translation setting = "empty string"
    translation = ""
    # letter is known by python and will cause it to look at each letter individually
    for letter in phrase:
        # dont need to , AEIOUaeiou because we specified for letter so it is checking each letter not phrase
        if letter.lower() in "aeiou": # checking lower case letters
            if letter.isupper():# checking upper cse letters
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a Phrase: ")))


