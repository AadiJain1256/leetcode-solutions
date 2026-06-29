class Solution(object):
    def twoSum(self, nums, target):
        hash={}
        for i in range(len(nums)):
            hash[nums[i]]=i
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in hash and hash[comp]!=i:
                return [i,hash[comp]]

        return []