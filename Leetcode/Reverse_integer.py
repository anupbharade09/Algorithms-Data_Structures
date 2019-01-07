import math
def reverse_int(a):
    n = len(str(a))
    l = list(str(a))
    if a <0:
        l.remove('-')
        l.append('-')
    mid= math.floor(n/2)
    i=0
    j=n-1
    while i < mid and j >= mid:
        l[i],l[j]=l[j],l[i]
        i += 1
        j -= 1


    return ''.join(l)

try:
    a = int(input('Please enter number: '))
    print(reverse_int(a))
except ValueError:
    print("That's not an int!")