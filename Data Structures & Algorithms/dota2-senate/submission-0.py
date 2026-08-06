class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        count = 0
        i = 0
        
        while i < len(senate):
            party = senate[i]
            if party == "R":
                if count < 0:
                    senate.append("D")
                count+=1
            else:
                if count > 0:
                    senate.append("R")
                count -= 1
            i += 1
        
        return "Radiant" if count > 0 else "Dire"
            