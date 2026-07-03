class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i=0
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
              continue
            left=i+1
            right=len(nums)-1
           
            while left<right:
                sum=nums[left]+nums[right]
                if sum==-nums[i]:
                    result.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif sum>-nums[i]:
                    right-=1
                elif sum<-nums[i]:
                    left+=1

        return result