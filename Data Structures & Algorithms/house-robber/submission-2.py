class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {} # i -> max achievable from i onwards
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            value = max(dfs(i+1), nums[i] + dfs(i+2))
            dp[i] = value
            
            return value	

        return dfs(0)
