class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def adder(sums, i, cur):
            if sums == target:
                ans.append(cur.copy())
                return
            if i >= len(nums) or sums > target:
                return

            cur.append(nums[i])
            adder(sums+nums[i], i+1, cur)

            cur.pop()
            k=1
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            adder(sums, i+1, cur)

            
        adder(0, 0, [])

        return ans

        # 1, 2, 2, 4, 5, 6, 9

