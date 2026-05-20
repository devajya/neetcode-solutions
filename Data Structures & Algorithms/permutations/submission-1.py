class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(curr_path, visited):
            if len(curr_path) == len(nums):
                ans.append(list(curr_path))
                return

            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                curr_path.append(nums[i])
                backtrack(curr_path, visited)
                curr_path.pop()
                visited[i] = False
            
        backtrack([], [False]*len(nums))
        return ans