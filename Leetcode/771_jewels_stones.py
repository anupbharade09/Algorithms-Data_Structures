class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # Dictionary to keep track of all jewels
        dict_jewels = {}
        for i in J:
            dict_jewels[i]= 0

        # Iterating over each element and incrementing count
        for j in S:
            if j in dict_jewels:
                dict_jewels[j] = dict_jewels[j] +1

        # returning sum of count values
        return sum(dict_jewels.values())


print(Solution().numJewelsInStones('aA','aAAbbbbb'))
