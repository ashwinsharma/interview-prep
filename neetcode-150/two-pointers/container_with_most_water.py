"""
Submission Link: https://leetcode.com/problems/container-with-most-water/submissions/1676218808
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1

        while l < r:
            hl = height[l]
            hr = height[r]
            d = r - l
            a = min(hl, hr) * d
            max_area = max(max_area, a)

            if hl <= hr:
                l += 1
            else:
                r -= 1
            
        return max_area
