'''You are given an array of characters and a string S. Write a 
function to return the string S with all the
characters from the array removed.'''


def remove_char(arr: list, str: str):
    result = ''
    for char in str:
        if char not in arr:
            result += char

    return result


print(remove_char(['H', 'e', 'd'], 'Hello World'))
