def rem_dup(A):
    elem={}
    c=0

    for i in range(len(A)):
        if A[i] in elem:
            elem[A[i]] = elem[A[i]]+1
        else:
            elem[A[i]]= c

    print(len(elem))

rem_dup(['1','1','2','1','1'])