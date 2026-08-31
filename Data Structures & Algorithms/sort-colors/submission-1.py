class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(3):
            for j in range(len(nums)):
                if nums[j] == i:
                    nums[left],nums[j] = nums[j],nums[left]
                    left += 1
            
