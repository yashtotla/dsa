import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        topK = []
        for num in nums:
            heapq.heappush(topK, num)
            if len(topK) == k+1:
                heapq.heappop(topK)
        return heapq.heappop(topK)