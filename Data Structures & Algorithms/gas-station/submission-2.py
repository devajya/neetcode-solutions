class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        trips = [j-i for i,j in zip(cost, gas)]
        if sum(trips) < 0: 
            return -1
        
        ans = 0
        tot_gas = 0

        for i in range(len(trips)):
            tot_gas += trips[i]

            if tot_gas < 0:
                tot_gas = 0
                ans = i+1
                
        return ans
