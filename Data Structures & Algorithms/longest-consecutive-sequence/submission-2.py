class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_len = 0

        for num in unique:
            if num -1 not in unique:
                curr = num
                curr_len = 1

                while curr + 1 in unique:
                    curr += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)

        return max_len
            
