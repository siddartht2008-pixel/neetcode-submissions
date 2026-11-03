class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        m = 0
        for i in range(0,len(nums)-1):
            if nums[i]== nums[i+1]:
                m += 1
        if m>0:
            return True
        else :
            return False

