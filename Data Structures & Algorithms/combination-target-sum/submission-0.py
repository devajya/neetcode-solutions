class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def adder(i, cur, sums):
            if sums == target:
                ans.append(cur.copy())
                return
            if i >= len(nums) or sums > target:
                return
            
            cur.append(nums[i])
            adder(i, cur, sums+nums[i])
            cur.pop()
            adder(i+1, cur, sums)

        adder(0, [], 0)
        return ans