# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?
#
# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
#
# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7


def string_to_number(s):
    # your code here
    try:
        toint = int(s)
        return toint
    except ValueError:
        print("You should enter only numbers")


s = input("Input the string to convert into integer: ")
while s.isdigit() == False:
    s = input("Input only numbers to convert into integer: ")
else:
    result = string_to_number(s)
    print(f"Now {result} is an integer")

