class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sta=[]
        pairs={"(" :")","[":"]","{":"}"}
        for start in range(len(s)):
            
            if s[start] =="(" or s[start]=="[" or s[start]=="{":
                sta.append(s[start])
            else:
                if not sta or pairs[sta[-1]] != s[start]:
                    return False
                sta.pop()
        return len(sta)==0