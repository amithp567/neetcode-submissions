class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for item in strs:
            key = str(sorted(item))

            if key in hashmap:
                hashmap[key].append(item)
            else:
                hashmap[key] = []
                hashmap[key].append(item)

        return list(hashmap.values())
        