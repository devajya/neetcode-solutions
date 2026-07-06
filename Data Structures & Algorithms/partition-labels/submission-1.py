class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i
        
        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size+=1
            end = max(end, last_idx[c])

            if end == i:
                res.append(size)
                size=0
        return res