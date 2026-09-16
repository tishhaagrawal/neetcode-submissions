class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: #because we made all the weights -ve
                heapq.heappush(stones, first - second)
        if stones: return -heapq.heappop(stones)
        else: return 0


        