class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSoFar = 1
        minSoFar = 1
        ans = nums[0]

        for num in nums:
            tempMaxStore = maxSoFar * num
            maxSoFar = max(num*maxSoFar, num*minSoFar, num)
            minSoFar = min(tempMaxStore, num * minSoFar, num)
            ans = max(ans, maxSoFar)
            print(ans)

        return ans