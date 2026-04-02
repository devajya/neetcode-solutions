from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxi = -1
        for c in counts:
            maxi = max(maxi, counts[c])
        
        endOffsetForDiffElementsSameMax = 0
        for c in counts:
            endOffsetForDiffElementsSameMax += 1 if counts[c] == maxi else 0
        
        # Format - 
        # A _ _ _ A _ _ _ A (number of elemes with same maxi)
        
        numGaps = maxi-1
        gapLen = n+1 # including element

        ans = numGaps * gapLen + endOffsetForDiffElementsSameMax
        return max(len(tasks), ans)
        