class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {} # (index, turn) -> (final score[optimal play])
        def dfs(i, a_turn):
            if i == len(stoneValue):
                return 0
            if (i, a_turn) in dp:
                return dp[(i, a_turn)]
            
            score = 0
            ans = float("-inf") if a_turn else float("inf")
            
            for j in range(i, min(len(stoneValue), i+3)):
                if a_turn:
                    score += stoneValue[j]
                    ans = max(ans, score + dfs(j+1, not a_turn))
                else:
                    score -= stoneValue[j]
                    ans = min(ans, score + dfs(j+1, not a_turn))
            
            dp[(i, a_turn)] = ans
            return ans


        sc = dfs(0, True)
        if sc == 0:
            return "Tie"
        
        return "Alice" if sc > 0 else "Bob"