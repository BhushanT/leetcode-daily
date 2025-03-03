class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new_nums = []

        for num in nums:
            if num < pivot:
                new_nums.append(num)

        for num in nums:
            if num == pivot:
                new_nums.append(num)

        for num in nums:
            if num > pivot:
                new_nums.append(num)

        return new_nums