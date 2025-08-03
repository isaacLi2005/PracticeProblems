class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False
        
        halfSum = totalSum // 2

        reachable = {0}
        for num in nums:
            new = {s + num for s in reachable if s + num <= halfSum}
            reachable = reachable.union(new)
        
            if halfSum in reachable:
                return True
        return False
