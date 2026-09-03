class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = sorted(set(nums))

        if len(unique) == 0:
            return 0

        current_len = 1
        max_len = 1
        prev = unique[0]
        for curr in range(1, len(unique)):
            if prev + 1 == unique[curr]:
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)

            prev = unique[curr]

        return max_len
            
