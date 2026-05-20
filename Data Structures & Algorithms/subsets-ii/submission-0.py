class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(start_idx, curr_path):
            ans.append(list(curr_path))
            if start_idx >= len(nums):
                return
            
            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i-1]:
                    continue
                curr_path.append(nums[i])
                backtrack(i+1, curr_path)
                curr_path.pop()
                
        backtrack(0, [])
        return ans