from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count)

            hashmap[key].append(word)
        
        return list(hashmap.values())
        