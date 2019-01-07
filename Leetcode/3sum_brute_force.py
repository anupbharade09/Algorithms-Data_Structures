def sum3(A):
    B= []
    for i in A:
        for j in range(i+1, len(A)):
            for k in range(j+1, len(A)):
                if A[i]+A[j]+A[k] == 0:
                    if sorted([A[i],A[j],A[k]]) not in B:
                        B.append(sorted([A[i],A[j],A[k]]))
    print(B)

sum3([-1, 0, 1, 2, -1, -4])