class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()
        ans = 0

        for num in nums:
            store.add(num)


        for num in store:
            can_max_len = 1
            temp = num-1

            while temp in store:
                can_max_len += 1
                temp-=1

            ans = max(ans, can_max_len)
        
        return ans