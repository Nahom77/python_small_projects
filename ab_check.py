def ab_check(strParam):
    for index, char in enumerate(strParam):
        # print()
        if char == 'a' and strParam[index+4] == 'b':
            return True

    return False


print(ab_check("Lauraso b"))
