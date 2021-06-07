

luckey_numbers = [2, 4, 6, 8, 10, 12, 14 ,16, 18, 20]
friends = ["Toby", "Brian", "Harry Pothead", "Frank"]
     
        # add name/number to list
        # .append adds to end of list
friends.append("creed")
        # insert into specific location 
        # item will be inserted before the index location selected
friends.insert(2,"crazy old man")
        # remove items from list
friends.remove("Harry Pothead")
        # add stuff to a list
friends.extend(luckey_numbers)
    # friends.clear() will clear list and start from scratch
        # removes item from end of list
friends.pop()

        # find stuff
        # .count counts amount of times found
        # .sort sorts alphabeticly
        # .reverse reverses order
        # copy
            # friends2 = friends
print(friends.index("Toby"))

print(friends)

