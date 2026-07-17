class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def ceilK(k):
            counts = defaultdict(int)
            ans = 0
            i = 0

            for j in range(len(nums)):
                counts[nums[j]] += 1
                if counts[nums[j]] == 1:
                    k-=1
                while k < 0:
                    counts[nums[i]] -=1
                    if counts[nums[i]] == 0:
                        k+=1
                    i+=1
                ans += (j-i+1)

            return ans
        
        return ceilK(k) - ceilK(k-1)