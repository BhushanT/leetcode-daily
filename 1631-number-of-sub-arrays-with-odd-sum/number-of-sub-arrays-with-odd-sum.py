from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Initialize to 1 to count empty prefix sum
        total_count = 0
        prefix_sum = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                total_count += odd_count  # Even prefix sum can extend odd subarrays
                even_count += 1
            else:
                total_count += even_count  # Odd prefix sum can extend even subarrays
                odd_count += 1

            total_count %= MOD

        return total_count
