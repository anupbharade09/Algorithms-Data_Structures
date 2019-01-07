def div(dividend,divisor):
    c=0
    while divisor <= dividend:
        if divisor == dividend:
            print(c)
            return c
        elif divisor < dividend:
            dividend -= divisor
            c += 1
    print(c)

div(7,3)