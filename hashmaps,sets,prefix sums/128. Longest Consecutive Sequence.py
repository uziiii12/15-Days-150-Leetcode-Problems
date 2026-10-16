class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sets = set(nums)
        longest = 0

        for num in sets:
            if num - 1 not in sets:
                count = 1
                curr = num

                while curr + 1 in sets:
                    curr += 1
                    count += 1

                longest = max(longest, count)

        return longest