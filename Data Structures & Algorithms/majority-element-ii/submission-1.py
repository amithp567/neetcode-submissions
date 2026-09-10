class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums) / 3

        hashmap = {}
        for value in nums:
            hashmap[value] = hashmap.get(value, 0) + 1
        
        res = []

        for i,v in hashmap.items():
            if v>majority:
                res.append(i)
        return res

