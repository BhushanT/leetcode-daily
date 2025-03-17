class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs = set()

        for num in nums:
            if num in pairs:
                pairs.remove(num)
            else:
                pairs.add(num)

        if len(pairs) != 0:
            return False
        else:
            return True