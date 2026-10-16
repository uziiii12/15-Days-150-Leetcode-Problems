class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            total=0
            for j in range(i,len(nums)):
                total+=nums[j]
                arr.append(total)
        return max(arr)           
