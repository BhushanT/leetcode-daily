class Solution:
    def findLHS(self, nums: List[int]) -> int:
        answer = 0 
        count = Counter(nums)
        for key in count:
            if key + 1 in count:
                answer = max(answer, count[key] + count[key + 1])
        return answer