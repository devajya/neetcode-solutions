class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        def chooser(idx):
            if idx>=len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[idx])
            chooser(idx+1)
            cur.pop()
            chooser(idx+1)

        chooser(0)

        return ans
        

