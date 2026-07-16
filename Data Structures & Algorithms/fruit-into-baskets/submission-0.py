class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        i, curr, ans = 0, 0, 0
        maps = defaultdict(int) 

        for j in range(0, len(fruits)):
            maps[fruits[j]] += 1
            curr += 1
            while len(maps) > 2:
                maps[fruits[i]] -= 1
                curr -= 1
                if not maps[fruits[i]]:
                    maps.pop(fruits[i])
                i+=1

            ans = max(ans, curr)
        return ans

                
