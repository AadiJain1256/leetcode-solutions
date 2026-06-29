class Solution(object):
    def longestConsecutive(self, nums):

        count=1
        max_length=1
        if not nums:
            return 0
        nums=sorted(list(nums))
        
        for a in range(len(nums)-1):
            if nums[a+1]==nums[a]+1:
                count+=1
                max_length=max(count,max_length)
            elif nums[a+1]==nums[a]:
                pass
            else:
                count=1
        return max_length