class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []

        for num in nums:
            if num not in arr:
                arr.append(num)

        nums[:len(arr)] = arr
        return len(arr)