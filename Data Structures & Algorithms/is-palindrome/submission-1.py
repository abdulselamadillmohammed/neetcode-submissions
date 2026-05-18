class Solution:
    def isPalindrome(self, s: str) -> bool:
        tot = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        s = s.lower()
        s = [i for i in s if i in tot]
        l,r = 0, (len(s) - 1)
        while l < r:
            if s[l] != s[r]:
                return False
            l +=1
            r -= 1
        return True