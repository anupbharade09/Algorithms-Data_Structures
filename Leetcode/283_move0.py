class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(nums[i])
        return nums

a= Solution().moveZeroes([0,1,2,3,0])
print(a)