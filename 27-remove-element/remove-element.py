class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for i,elem in enumerate(nums):
            if elem!=val:
                nums[c]=elem
                c+=1
        return c
        