class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p, q = 0, len(heights) - 1
        res = 0

        while p < q:
            area = min(heights[p], heights[q]) * (q - p)
            res = max(res, area)
            if heights[p] <= heights[q]:
                p += 1
            else:
                q -= 1
        return res