class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(start_idx, curr_sum, curr_path):
            if curr_sum == target:
                ans.append(list(curr_path))
                return
            if curr_sum > target:
                return

            for i in range(start_idx, len(candidates)):
                if i>start_idx and candidates[i] == candidates[i-1]:
                    continue
                
                curr_path.append(candidates[i])
                backtrack(i+1, curr_sum+candidates[i], curr_path)
                curr_path.pop()

        backtrack(0, 0, [])
        return ans