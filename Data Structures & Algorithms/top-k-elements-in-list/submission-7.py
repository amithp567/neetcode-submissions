class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        sorted_hashmap = sorted(
            hashmap.items(),
            key = lambda x: x[1],
            reverse=True
        )

        for key,value in sorted_hashmap[:k]:
            res.append(key)

        return res
