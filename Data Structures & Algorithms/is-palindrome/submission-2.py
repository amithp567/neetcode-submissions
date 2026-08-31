class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = ""

        for i in s:
            if i.isalnum():
                if i.isalpha():
                    q += i.lower()
                else:
                    q += i
        l, r = 0, len(q)-1

        while l < r:
            if q[l] != q[r]:
                return False
            l += 1
            r -= 1
        return True                

        