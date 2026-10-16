class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        arr = []

        for i in nums:
            if i not in arr:
                arr.append(i)

        for i in arr:
            if nums.count(i) > len(nums) // 2:
                return i