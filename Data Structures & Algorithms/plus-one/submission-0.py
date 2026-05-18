class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = [str(i) for i in digits]
        return [i for i in str(int("".join(a)) + 1)]