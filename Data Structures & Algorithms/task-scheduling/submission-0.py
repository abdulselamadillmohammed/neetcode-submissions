class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0 
        q = deque()
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        while maxHeap or q:
            time += 1
            if maxHeap:
                value = heapq.heappop(maxHeap)
                value += 1
                if value:
                    q.append([value, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time