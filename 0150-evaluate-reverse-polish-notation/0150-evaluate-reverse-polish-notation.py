import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        sta=[]
        ops={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':lambda a,b:(abs(a)//abs(b))*(-1 if (a<0)!= (b<0) else 1),}
        for token in tokens:
            if token not in ops:
                sta.append(int(token))
            else:
                right=sta.pop()
                left=sta.pop()
                sta.append(ops[token](left,right))
        return sta[-1]