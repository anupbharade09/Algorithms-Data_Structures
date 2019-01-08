class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums != []:
            for i in [int_elem for int_elem in range(1,max(nums)+2)]:
                if i in nums:
                    continue
                else:
                    return i
        else:
            return 1

print(Solution().firstMissingPositive([0]))