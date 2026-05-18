class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        container = [[] for i in range(( len(nums) +1)) ]
        count = Counter(nums)
        for key, value in count.items():
            container[value].append(key)
        
        total = []
        for i in container:
            for j in i:
                total.append(j)
        return total[::-1][:k]
        