class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return not (len(nums) == len(set(nums)))

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            
        
        for k,v in hashmap.items():
            if v > 1:
                return True
        return False