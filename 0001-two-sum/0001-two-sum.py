class Solution(object):
    def twoSum(self, nums, target):
        dict={}

        for a in range(len(nums)):
            
            need = target-nums[a]
            if need in dict:
                return [a,dict[need]]

            dict[nums[a]]=a

            