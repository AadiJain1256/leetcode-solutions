class Solution(object):
    def groupAnagrams(self, strs):
        dicta={}
        lista=[]
        for a in strs:
            key=''.join(sorted(a))
            if key not in dicta:
                dicta[key]=[a]
            else:
                dicta[key].append(a)
        for key,values in dicta.items():
            lista.append(values)
        return lista