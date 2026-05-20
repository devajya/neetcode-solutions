class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(start_idx, curr_path):
            
            ans.append(list(curr_path))

            for i in range(start_idx, len(nums)):
                curr_path.append(nums[i])
                backtrack(i+1, curr_path)
                curr_path.pop()

        backtrack(0, [])
        return ans