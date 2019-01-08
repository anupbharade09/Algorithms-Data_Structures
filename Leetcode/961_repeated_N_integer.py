class Solution:
    def repeatedNTimes(A):

        if len(A) < 4 or len(A) >10000 or len(A)%2 != 0:
            print('Length of the list should be greater than 3 and lesser than 10000 and even number ')
        else:
            n = len(A)/2
            d = {}

            for i in A:
                if i in d:
                    d[i] = d[i]+1
                else:
                    d[i] = 1
            for j in d:
                if d[j] == n:
                    return j

A= [1,2,3,3]

Solution.repeatedNTimes(A)