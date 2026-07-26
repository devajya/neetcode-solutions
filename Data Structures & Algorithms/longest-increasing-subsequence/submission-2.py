class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [1]*n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    ans[i] = max(ans[i], 1+ans[j])
        
        return max(ans)