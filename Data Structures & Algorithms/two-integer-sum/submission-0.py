class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 =[]
        l = 0
        for i in range(0,len(nums)):
            nums1.append(target-nums[i])
        for i in range(0,len(nums)):
            if nums[i] in nums1:
                l = i
        m = nums1.index(nums[l])        
        s = [m,l]
        return s      
        