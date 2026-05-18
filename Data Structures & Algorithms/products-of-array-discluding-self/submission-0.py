class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(res)):
                if j != i:
                    res[j] *= nums[i]
        return res