import math
class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a


        if len(nums)==1:
            return 1
        else:
            best=0
            for start in range(len(nums)):
                prod=1
                gcd_value=0
                lcm_value=1
                for end in range(start,len(nums)):
                    gcd_value=gcd(gcd_value,nums[end])
                    lcm_value=(lcm_value // gcd(lcm_value,nums[end]))*nums[end]
                    prod*=nums[end]

                    if prod==gcd_value* lcm_value:
                        best=max(best,end-start+1)
            return best