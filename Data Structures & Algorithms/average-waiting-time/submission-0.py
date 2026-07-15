class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        wait = 0
        for arr, dur in customers:
            start = max(arr, t)
            end = start + dur
            wait += (end-arr)
            t = end

        return wait / len(customers)