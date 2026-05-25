'''
read the array of strings stored in strArr which will contain only two elements, both of which will represent an array of positive integers.

Example:
if strArr = ["[1, 2, 5, 6]", "[5, 2, 8, 11]"]``

then both elements in the input represent two integer arrays, and your goal for this challenge is to add the elements in corresponding locations from both arrays.

For the example input, your program should do the following additions: [(1 + 5), (2 + 2), (5 + 8), (6 + 11)] which then equals [6, 4, 13, 17].

Your program should finally return this resulting array in a string format with each element separated by a hyphen: 6-4-13-17.

If the two arrays do not have the same amount of elements, then simply append the remaining elements onto the new array (example shown below).

Both arrays will be in the format: [e1, e2, e3, ...] where at least one element will exist in each array.
'''


def array_matching(str):
    l1 = [int(i) for i in str[0][1:-1].split(',')]
    l2 = [int(i) for i in str[1][1:-1].split(',')]

    if len(l1) != len(l2):
        n = max(len(l1), len(l2))
        l1.extend([0] * (n - len(l1)))
        l2.extend([0] * (n - len(l2)))

    res = [str(a+b) for a, b in zip(l1, l2)]

    return "-".join(res)


array_matching(['[1,2,3]'])
