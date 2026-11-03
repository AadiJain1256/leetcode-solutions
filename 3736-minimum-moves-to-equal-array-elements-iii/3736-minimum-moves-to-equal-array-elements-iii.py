class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_i=nums[0]
        n=len(nums)
        sum=0
        for i in range(0,n):
            
            if max_i<nums[i]:
                max_i=nums[i]

        for i in range(0,n):
            sum+=max_i-nums[i]

        return sum
        