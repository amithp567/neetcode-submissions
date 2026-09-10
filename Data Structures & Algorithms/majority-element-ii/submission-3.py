class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        left = 0
        res = []

        while left<len(nums):
            right = left + 1
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            
            if right - left > len(nums)//3:
                res.append(nums[left])
            
            left = right
        return res


