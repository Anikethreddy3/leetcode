class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            n=target-nums[i]
            try:
                j=nums.index(n,i+1)
                return [i,j]
            except ValueError:
                continue
