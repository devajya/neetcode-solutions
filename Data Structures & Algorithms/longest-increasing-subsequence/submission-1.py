class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            lis = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    lis = max(lis, 1+dfs(j))
            
            dp[i] = lis
            return dp[i]
        
        return max(dfs(i) for i in range(n))