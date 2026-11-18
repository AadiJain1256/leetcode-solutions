class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        waiting=[]
        for i,temp in enumerate(temperatures):
            while waiting and temperatures[waiting[-1]]<temp:
                previous_day=waiting.pop()
                answer[previous_day]=i-previous_day

            waiting.append(i)
        return answer