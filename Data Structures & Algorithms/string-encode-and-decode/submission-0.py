class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += (str(len(word))  + "#" + word)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num = ""
        while i != len(s):
            while s[i] != "#":
                num += s[i]
                i +=1
            i += 1
            res.append(s[ i:i+int(num) ])
            i += int(num)
            num = ""
        return res