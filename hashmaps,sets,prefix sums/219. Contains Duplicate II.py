class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        map={}
        for i in range(len(nums)):
            if nums[i] in map:
                if i - map[nums[i]] <=k:
                    return True
            map[nums[i]]=i
        return False            