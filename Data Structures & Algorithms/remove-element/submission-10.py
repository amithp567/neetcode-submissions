class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        lenght = len(nums)

        while index < lenght:
            if nums[index] == val:
                lenght -= 1
                nums[index] = nums[lenght]
            else:
                index += 1
        return lenght
