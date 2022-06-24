# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


def solution1(s):
    z = []
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            z.append(s[i: i + 2])
        print(z)
    elif len(s) % 2 == 1:
        for i in range(0, len(s), 2):
            z.append(s[i: i + 2])
        z[-1] = z[-1] + "_"
        print(z)


def solution2(s):
    if len(s) <= 1:
        if len(s) == 0:
            return []
        else:
            return [s + '_']
    return [s[0:2]] + solution2(s[2:])
