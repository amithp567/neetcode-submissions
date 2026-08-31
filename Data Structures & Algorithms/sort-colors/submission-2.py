class Solution:
    def sortColors(self, nums: List[int]) -> None:
        f = s = 0
        t = len(nums)-1

        while s <= t:
            if nums[s] == 0:
                nums[f], nums[s] = nums[s], nums[f]
                f += 1
                s += 1
            elif nums[s] == 1:
                s += 1
            else:
                nums[s], nums[t] = nums[t], nums[s]
                t -= 1