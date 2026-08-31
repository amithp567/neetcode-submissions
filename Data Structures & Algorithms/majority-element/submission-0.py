
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums)//2
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) +1
        
        for value in hashmap:
            if hashmap[value] >half:
                return value
        