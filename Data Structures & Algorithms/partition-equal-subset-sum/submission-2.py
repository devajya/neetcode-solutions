class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0:
            return False
        
        target = s // 2

        dp = {}
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i>=len(nums):
                return False
            if (i, target) in dp:
                return dp[(i, target)]

            l1 = dfs(i+1, target)
            l2 = dfs(i+1, target-nums[i])

            dp[(i, target)] = l1 or l2
            return dp[(i, target)]

        return dfs(0, target)