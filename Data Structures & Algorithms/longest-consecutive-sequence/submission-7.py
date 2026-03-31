class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()

        for n in nums:
            store.add(n)

        ans = 0
        for n in nums:
            if n-1 in store:
                continue

            count = 0
            while n in store:
                n+=1
                count+=1
            ans = max(ans, count)

        return ans