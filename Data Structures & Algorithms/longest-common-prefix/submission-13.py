class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in range(1, len(strs)):
            index = 0
            while index < min(len(prefix), len(strs[s])):
                if prefix[index] != strs[s][index]:
                    break
                
                index += 1
            prefix = prefix[:index]
        return prefix