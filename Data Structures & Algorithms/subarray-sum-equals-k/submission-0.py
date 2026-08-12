class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        pref_sum_to_frq = {0:1}
        for num in nums:
            current_sum += num
            target = current_sum - k
            ans += pref_sum_to_frq.get(target, 0)
            pref_sum_to_frq[current_sum] = 1 + pref_sum_to_frq.get(current_sum, 0)
        
        return ans