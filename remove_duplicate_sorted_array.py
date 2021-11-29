class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            if i<=len(nums)-2 and nums[i] == nums[i+1]:
                continue
            nums[c]=nums[i]
            c+=1
        return c