class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new_nums = [0] * len(nums)
        before_count = 0
        pivot_count = 0
        after_count = 0

        for num in nums:
            if num < pivot:
                before_count+=1
            elif num == pivot:
                pivot_count+=1
            else:
                after_count+=1

            b = 0
            a = before_count + pivot_count

        for i,num in enumerate(nums):
            if num < pivot:
                new_nums[b] = num
                b+=1
            elif num > pivot:
                new_nums[a] = num
                a+=1

        for i in range(pivot_count):
            new_nums[i + before_count] = pivot

        return new_nums