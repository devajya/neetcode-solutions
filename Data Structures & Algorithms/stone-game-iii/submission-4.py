class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        sys.setrecursionlimit(100000)
        dp = {} #(index, whose turn):
        def dfs(i, a_turn):
            if i == len(stoneValue):
                return 0
            if (i, a_turn) in dp:
                return dp[(i, a_turn)]

            score = 0
            ans = float("-inf") if a_turn else float("+inf")
            for j in range(i, min(i+3, len(stoneValue))):
                if a_turn:
                    score += stoneValue[j]
                    ans = max(ans, score + dfs(j+1, not a_turn))
                else:
                    score -= stoneValue[j]
                    ans = min(ans, score+dfs(j+1, not a_turn))
            
            dp[(i, a_turn)] = ans
            return ans

        ans = dfs(0, True)
        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        return "Tie"