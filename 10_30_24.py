from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # DP arrays for the longest increasing subsequence from left and right
        left_dp = [1] * n
        right_dp = [1] * n
        
        # Calculate left_dp - longest increasing subsequence up to each point
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left_dp[i] = max(left_dp[i], left_dp[j] + 1)
        
        # Calculate right_dp - longest decreasing subsequence from each point
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right_dp[i] = max(right_dp[i], right_dp[j] + 1)
        
        # Calculate minimum removals to make a mountain array
        min_removals = n
        for i in range(1, n - 1):
            if left_dp[i] > 1 and right_dp[i] > 1:  # Valid peak
                mountain_length = left_dp[i] + right_dp[i] - 1
                min_removals = min(min_removals, n - mountain_length)
        
        return min_removals
