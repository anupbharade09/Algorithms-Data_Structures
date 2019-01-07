def palindrome(str):
    a = []
    for i in range(len(str)):
        a.append(str[i])
    k=0
    rev = []
    j= len(a)-1
    while j >= 0:
        rev.append(a[j])
        #k += 1
        j -= 1
    reverse = ''.join(rev)
    if reverse == str:
        print('true')
    else:
        print('false')