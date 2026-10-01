class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        heap = []

        my_map = defaultdict(int)
        for num in nums:
            my_map[num] += 1
        for num in my_map.keys():
            heapq.heappush(heap,(my_map[num], num))
            if len(heap)>k:
                heapq.heappop(heap)
        res =[]
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res
        