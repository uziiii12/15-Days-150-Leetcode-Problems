class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sets = {0: 1}
        curr = 0
        count = 0

        for num in nums:
            curr += num
            need = curr - k

            if need in sets:
                count += sets[need]
            sets[curr] = sets.get(curr, 0) + 1

           

        return count