class Solution(object):
    def containsDuplicate(self, nums):
        a=len(nums)
        dicta={}
        for i in range(0,len(nums)):
            
            if nums[i] in dicta:
                dicta[nums[i]]+=1
            else:
                dicta[nums[i]]=1

        for i in dicta:
            if dicta[i]>=2:
                return True
        return False