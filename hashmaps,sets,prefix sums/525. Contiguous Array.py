class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sets = {0: -1}
        curr = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1

            if curr in sets:
                longest = max(longest, i - sets[curr])
            else:
                sets[curr] = i

        return longest