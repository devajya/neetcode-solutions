class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(perms, picks):
            if len(perms) == len(nums):
                ans.append(perms.copy())
                return
            for i in range(len(nums)):
                if not picks[i]:
                    perms.append(nums[i])
                    picks[i] = True
                    backtrack(perms, picks)
                    perms.pop()
                    picks[i] = False
        backtrack([], [False] * len(nums))
        return ans