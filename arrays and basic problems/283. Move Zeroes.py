class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[]
        for i in nums:
            if i != 0:
                arr.append(i)
        for j in nums:
            if j ==0:
                arr.append(j)
        nums[:]=arr
        return arr                            