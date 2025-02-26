class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        prefixSum = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefixSum[i] = nums[i]
            else:
                prefixSum[i] = prefixSum[i-1] + nums[i]

        print(prefixSum)
        res = max(max(prefixSum),0) - min(min(prefixSum),0)

        return res
        