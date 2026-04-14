class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        def adder(cur, i, sums):
            if sums == target:
                ans.append(cur.copy())
                return
            if i >= len(nums) or sums > target:
                return

            cur.append(nums[i])
            adder(cur, i+1, sums+nums[i])

            cur.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1 
            adder(cur, i+1, sums)

        adder([], 0, 0)

        return ans