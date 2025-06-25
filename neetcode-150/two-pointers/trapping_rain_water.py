"""
Submission Link: https://leetcode.com/problems/trapping-rain-water/submissions/1676525174
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        # first pass - forwards
        water, temp = 0, 0      # total water counter & temp counter
        anchor, scan = 0, 0     # the two pointers
        n = len(height)
        
        while scan < n:
            if height[scan] < height[anchor]:
                temp += height[anchor] - height[scan]
                scan += 1
            else:
                water += temp
                temp = 0
                anchor = scan
                scan += 1
        
        # second pass - backwards
        tallest = anchor
        anchor, scan = n-1, n-1
        temp = 0
        
        while scan >= tallest:
            if height[scan] < height[anchor]:
                temp += height[anchor] - height[scan]
                scan -= 1
            else:
                water += temp
                temp = 0
                anchor = scan
                scan -= 1
        
        return water
