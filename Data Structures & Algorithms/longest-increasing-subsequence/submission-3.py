class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        def dfs(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]

            ans = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    ans = max(ans, 1+dfs(j))
            
            dp[i] = ans
            return ans

        return max(dfs(i) for i in range(n))