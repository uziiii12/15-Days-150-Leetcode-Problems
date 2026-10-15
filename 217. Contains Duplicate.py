class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets=set()
        count=0
        for num in nums:
            if num in sets:
                return True
            sets.add(num)
            
        return False   