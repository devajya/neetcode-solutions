class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1

        sizes = [[] for i in range(len(nums)+1)]

        for num, c in count.items():
            sizes[c].append(num)

        ans = []
        for i in range(len(sizes)-1, 0, -1):
            for num in sizes[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans