class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        counts = {0: 1}
        prefix_sum = 0
        count = 0
    
        for num in nums:
            prefix_sum += num
            count += counts.get(prefix_sum - k, 0)
            counts[prefix_sum] = counts.get(prefix_sum, 0) + 1
    
        return count  