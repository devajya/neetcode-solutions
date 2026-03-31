class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        container = set()
        for i in nums:
            container.add(i)
        maxcount = min(1, len(container))

        for i in nums:
            num = i
            count=0
            while num-1 in container:
                num+=1
                count+=1
            maxcount = max(maxcount, count)

        return maxcount
        
