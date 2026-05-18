class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = nums[0]
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        while k:
            a = -heapq.heappop(nums)
            k -= 1
        
        return a