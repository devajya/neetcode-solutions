class Solution:
    sys.setrecursionlimit(100000)
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        # (index, alices_turn:Boolean) = Score of player
        def dfs(i, a_turn):
            if i>=len(stoneValue):
                return 0
            if (i, a_turn) in dp:
                return dp[(i, a_turn)]
            
            score = 0
            ans = float("-inf") if a_turn else float("+inf")
            for j in range(i, min(i+3, len(stoneValue))):
                if a_turn:
                    score += stoneValue[j]
                    ans = max(ans, score+dfs(j+1, not a_turn))
                else:
                    score -= stoneValue[j]
                    ans = min(ans, score+dfs(j+1, not a_turn))
            
            dp[(i, a_turn)] = ans
            return ans

        res = dfs(0, True)
        if res == 0:
            return "Tie"
        return "Alice" if res > 0 else "Bob"

