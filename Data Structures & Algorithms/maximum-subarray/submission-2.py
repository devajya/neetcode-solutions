class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        back = 0
        for i in range(0, len(nums)):
            if cur_sum < 0:
                back = i
                cur_sum = 0
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum