class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        maps = {0: -1}
        cur = 0

        for i, num in enumerate(nums):
            cur += num
            cur_rem = cur % k

            if cur_rem in maps:
                if i-maps[cur_rem]>=2:
                    return True
            else:
                maps[cur_rem] = i
            
        return False
                