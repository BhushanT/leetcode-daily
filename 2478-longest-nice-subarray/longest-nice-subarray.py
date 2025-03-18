from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        window_or = 0
        longest = 1
        
        for r in range(len(nums)):
            while (window_or & nums[r]) != 0:
                window_or ^= nums[l]
                l += 1
            
            window_or |= nums[r]
            longest = max(longest, r - l + 1)
        
        return longest
