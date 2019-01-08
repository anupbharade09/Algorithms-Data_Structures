class Solution:
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        A = list(s)
        i = 0
        j = len(A)-1
        while i < j:
            if A[i] not in vowels:
                i += 1
            elif A[j] not in vowels:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        print(''.join(A))

Solution().reverseVowels('abnA')