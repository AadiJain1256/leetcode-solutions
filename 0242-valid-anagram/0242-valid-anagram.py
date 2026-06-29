class Solution(object):
    def isAnagram(self, s, t):
        dicta={}
        if len(t)!=len(s):
            return False
        else:
            for a in s:
                if a in dicta:
                    dicta[a]+=1
                else:
                    dicta[a]=1
        for a in t:
            if a not in dicta:
                return False
            else:
                dicta[a]-=1

        for a in dicta.values():
            if a!=0:
                return False
            else:
                return True