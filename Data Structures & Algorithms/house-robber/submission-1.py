class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back, two_back = 0, 0
        for num in nums:
            we_rob = max(num+two_back, one_back)
            two_back = one_back
            one_back = we_rob
        
        return one_back
