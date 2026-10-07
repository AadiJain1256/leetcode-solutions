class Solution(object):
    def isAnagram(self, s, t):
        l={}
        if len(s)!=len(t):
            return False

        else:
            for a in range(len(s)):
                if s[a] not in l:
                    l[s[a]]=1
                else:
                    l[s[a]]+=1

            for a in range(len(t)):
                if t[a] not in l:
                    return False
                else:
                    l[t[a]]-=1

            for a in l:
                if l[a] !=0:
                    return False
            return True

