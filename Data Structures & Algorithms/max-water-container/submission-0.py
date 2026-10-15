class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = l = 0
        r = len(heights) - 1
        while l < r:
            l_shorter = True if heights[l] < heights[r] else False
            curr = min(heights[r], heights[l]) * (r - l)
            mx = max(curr, mx)
            if l_shorter:
                l += 1
            else:
                r -= 1
        return mx