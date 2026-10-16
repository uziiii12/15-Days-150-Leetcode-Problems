class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        sets={}
        for num in nums1:
            sets[num]=sets.get(num,0)+1

        arr =[]
        for num in nums2:
            if num in sets and sets[num]>0 :
                arr.append(num)
                sets[num]-=1
        return arr        