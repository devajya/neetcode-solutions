class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        pre_tech = 0 
        bonus = 0
        tracker = 0
        n = len(customers)
        i=0

        for j in range(0, n):
            if grumpy[j] == 1:
                tracker += customers[j]
            else:
                pre_tech += customers[j]

            if j-i+1 == minutes:
                bonus = max(bonus, tracker)
                tracker -= customers[i] if grumpy[i] == 1 else 0
                i+=1
        return pre_tech+bonus

