'''
For this challenge you are given a string and 
you should return the first character that is unique in the
entire string. For example:

    • If string is “hello henry” then the first non-repeating 
    character is the letter “o” because
    the first three characters in the string appear multiple times.
'''


def non_repeating_characters(str):
    hash = {}

    for char in str:
        if char not in hash:
            hash[char] = 1
        else:
            hash[char] += 1

    for c in str:
        if hash[c] == 1:
            return c

    return -1


print(non_repeating_characters('hello henry'))
