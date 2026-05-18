class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = float("inf")
        for i in range(len(nums)):
            if nums[i] == cur:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                if -nums[i] - nums[l] < nums[r]:
                    r-=1
                elif -nums[i] - nums[l] > nums[r]:
                    l += 1
                elif -nums[i] - nums[l] - nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            cur = nums[i]
        return res