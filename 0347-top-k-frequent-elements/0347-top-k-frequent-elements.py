class Solution(object):
    def topKFrequent(self, nums, k):
        num=list(nums)
        hasha={}
        result=[]
        for a in num:
            if a in hasha:
                hasha[a]+=1
            else:
                hasha[a]=1
        hasha=sorted(hasha.items(),key=lambda x:x[1],reverse=True)
        for a,b in hasha[:k]:
            result.append(a)
        return result
