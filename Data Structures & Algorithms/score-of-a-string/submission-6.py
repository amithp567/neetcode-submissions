class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        prev=ord(s[0])
        for i in range(1,len(s)):
            cur=ord(s[i])
            sum+=abs(cur-prev)
            prev=cur
        return sum
