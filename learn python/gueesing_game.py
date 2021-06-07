        # basic guessing game
secret_word = "winner"
guess = ""
        # setting guess limit
        # guess_count = 0 so count starts at 0 if it was set to 5 guess count would start at 5 
guess_count = 0
        # setting limit
guess_limit = 3
        # setting true false setting
out_of_guesses = False
        # while loop inut
        # != not equal to

while guess != secret_word and not (out_of_guesses):
        # adding count checker
        if guess_count <  guess_limit:
            # storing guess variable in empty sting above (guess = "")
            guess = input("Guess Please: ")
            # adding counter for guess
            guess_count += 1
        else:
            # setting out of guesses to true 
            out_of_guesses = True
if out_of_guesses:
     print("you loose!")
else:
    print("YOU WIN!!!!!!!!")

