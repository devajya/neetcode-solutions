class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 2, 4, 6]

        b = [1]
        a = [1]

        for i in range(1, len(nums)):
            b.append(b[-1]*nums[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            a.append(a[-1]*nums[i+1])

        a.reverse()
        ans = []

        for _a, _b in zip(a, b):
            ans.append(_a*_b)
        
        return ans

