class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        one_back, two_back = 0, 0
        for num in nums:
            we_rob = max(two_back+num, one_back)
            two_back = one_back
            one_back = we_rob
        
        return one_back