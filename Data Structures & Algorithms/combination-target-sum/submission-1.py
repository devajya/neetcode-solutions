class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(start_idx, curr_sum, curr_path):
            if curr_sum == target:
                ans.append(list(curr_path))
                return
            if curr_sum > target:
                return

            for i in range(start_idx, len(nums)):
                curr_path.append(nums[i])
                backtrack(i, curr_sum+nums[i], curr_path)
                curr_path.pop()

        backtrack(0, 0, [])
        return ans