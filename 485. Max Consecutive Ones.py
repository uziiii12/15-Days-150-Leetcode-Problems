class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = []
        count = 0

        for i in nums:
            if i == 1:
                arr.append(i)
                count = max(count, len(arr))
            else:
                arr = []

        return count