def string_periods(strParam):
    n = len(strParam)

    for size in range(n//2, 0, -1):
        if n % size == 0:
            k = strParam[:size]
            if k * (n // size) == strParam:
                return k

    return -1


print(string_periods('a'))
