class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        storage = {}

        for right in range(len(s)):
            storage[s[right]] = 1 + storage.get(s[right],0)
            while (right - left + 1) - max(storage.values()) > k:
                storage[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res