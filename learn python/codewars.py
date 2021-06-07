def disemvowel(string_):
    vowels = ('a', 'e', 'i', 'o', 'u',)
    for x in string_:
        if x in vowels:
            string_ = string_.replace(x, "")
    return string_
    

teststring = "This is a test string with several words\n"
print(disemvowel(teststring))