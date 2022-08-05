# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore
# letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

def is_isogram(string):
    # your code here
    string = string.lower()
    lstring = [letter for letter in string]
    if len(set(lstring)) == len(lstring):
        return True
    else:
        return False


print(is_isogram("okKla"))


# Make a program that filters a list of strings and returns a list with only your friends name in it.
#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be
# sure he's not...
#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
#
# i.e.
#
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
#
# Note: keep the original order of the names in the output.
def friend(x):
    # Code
    friend_list = list()
    for item in x:
        if len(item) == 4:
            friend_list.append(item)
    return friend_list


print(friend(["Baid", "Makron", "Bori", "Putin"]))