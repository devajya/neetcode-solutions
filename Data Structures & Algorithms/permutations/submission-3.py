class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(so_far, visited):
            if len(so_far) == len(nums):
                ans.append(list(so_far))
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                so_far.append(nums[i])
                backtrack(so_far, visited)
                visited[i] = False
                so_far.pop()

        backtrack([], [False for _ in range(len(nums))])
        return ans
