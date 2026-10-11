class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_value = []
        for index, value in enumerate(nums):
            key_value.append([value, index])
        key_value.sort()

        l, r = 0, len(nums)-1

        while l<r:
            current_sum = key_value[l][0] + key_value[r][0]

            if current_sum == target:
                return [
                    min(key_value[l][1],key_value[r][1]),
                    max(key_value[l][1],key_value[r][1])
                ]
            elif current_sum > target:
                r -= 1
            else:
                l += 1
        