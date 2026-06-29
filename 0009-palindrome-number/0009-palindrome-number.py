class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=0
        num=x
        while num>0:
            ld=num%10
            n=n*10+ld
            num=num//10
        return n==x
        