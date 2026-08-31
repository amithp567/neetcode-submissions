class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for char in t:
            if char in hashmap and hashmap[char] >0:
                hashmap[char] -= 1
            else:
                return False
        return True if sum(hashmap.values())==0 else False