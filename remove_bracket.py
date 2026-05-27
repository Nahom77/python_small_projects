def remove_brackets(strParam):
    closed_bracket = 0
    opened_bracket = 0

    for char in strParam:
        if char == '(':
            opened_bracket += 1
        else:
            closed_bracket += 1

    return abs(closed_bracket-opened_bracket)


print(remove_brackets("(())()((("))
