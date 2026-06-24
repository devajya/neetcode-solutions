class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total // 2

        # dp -> kth bit = 1 means sum k is achivable
        dp = 1 << 0 # sum = 0 is possible 

        for num in nums:
            dp |= dp << num

        return (dp & 1 << target) != 0