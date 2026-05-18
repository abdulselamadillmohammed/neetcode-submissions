class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        matches, l = 0,0
        need, window = {}, {}

        for i in range(len(s1)):
            need[s1[i]] = 1 + need.get(s1[i], 0)
            window[s2[i]] = 1 + window.get(s2[i], 0) 

        for c in need:
            if c in window and window[c] == need[c]:
                matches += 1

        for r in range(len(s1), len(s2)):

            if matches == len(need):
                return True

            c = s2[r]
            window[c] = 1 + window.get(c, 0)

            if c in need:
                if window[c] == need[c]:
                    matches += 1
                elif window[c] == need[c] + 1:
                    matches -= 1

            left_char = s2[l]
            
            if left_char in need:
                if window[left_char] == need[left_char]:
                    matches -=1
                elif window[left_char] == need[left_char] + 1:
                    matches += 1
            
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            l+= 1

        return matches == len(need)