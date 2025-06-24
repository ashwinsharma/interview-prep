"""
Submission Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1675320988

Sorting based solution (written by me)
Time Complexity: O(nlogn)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        sorted_nums = sorted(nums)
        c = 1
        maxC = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue
            elif sorted_nums[i] == sorted_nums[i-1] + 1:
                c += 1
            else:
                if c > maxC:
                    maxC = c
                c = 1
        
        if c > maxC:
            maxC = c
        
        return maxC
    
"""
Subission Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1675327304

Hashset based solution (from the editorial section)
Time Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
