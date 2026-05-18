class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lister = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    lister[i] = max(lister[i],1+lister[j])
        return max(lister)