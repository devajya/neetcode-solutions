class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def chooser(cur, i):
            if i > len(nums)-1:
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            chooser(cur, i+1)
            cur.pop()
            chooser(cur, i+1)
        
        chooser([], 0)
        return ans