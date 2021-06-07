            # key value pairs

month_conversions = {
    "jan": "january",
    "feb": "febuary",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december"
}

        # accessing dictionary

print(month_conversions["nov"])
        # invaid input prints none
print(month_conversions.get("luv"))
        # invalid input prints "text in quotes"
print(month_conversions.get("luv", "not a valid key"))