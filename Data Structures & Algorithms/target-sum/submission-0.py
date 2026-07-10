class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {} # (index, amount)
        def dfs(i, accum):
            if i == len(nums):
                return 1 if accum == target else 0

            if (i, accum) in dp:
                return dp[(i, accum)]
            
            add = dfs(i+1, accum+nums[i])
            sub = dfs(i+1, accum-nums[i])

            dp[(i, accum)] = add + sub

            return dp[(i, accum)]
        
        return dfs(0, 0)