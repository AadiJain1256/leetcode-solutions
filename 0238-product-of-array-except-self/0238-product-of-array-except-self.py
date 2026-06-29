class Solution(object):
    def productExceptSelf(self, nums):
        right=[0]*len(nums)
        left=[0]*len(nums)
        i=0
        product=1
        result=[]
        for i in range(len(nums)):
            left[i]=product
            product*=nums[i]
        product=1
        for i in range(len(nums)-1,-1,-1):
            right[i]=product
            product*=nums[i]
        for j in range(len(nums)):
            result.append(left[j]*right[j])
        return result 