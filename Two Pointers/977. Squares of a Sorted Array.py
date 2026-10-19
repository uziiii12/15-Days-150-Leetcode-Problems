class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr = []

        for num in nums:
            square = num * num
            arr.append(square)

        arr.sort()
        return arr
    




class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        arr = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                arr[pos] = nums[left] * nums[left]
                left += 1
            else:
                arr[pos] = nums[right] * nums[right]
                right -= 1

            pos -= 1

        return arr    