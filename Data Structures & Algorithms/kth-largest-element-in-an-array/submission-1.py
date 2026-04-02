import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:    
        nums = [-num for num in nums]
        heapq.heapify(nums)
        ans = -1
        while k>0:
            ans = heapq.heappop(nums)
            k-=1
        return -ans