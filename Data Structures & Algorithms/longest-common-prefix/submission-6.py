class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        j=0
        while j < min(len(strs[0]),len(strs[-1])):
            if strs[0][j] != strs[-1][j]:
                break
            j += 1
        
        return strs[0][:j]
                

        