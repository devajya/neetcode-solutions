class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idxr = {order[i]:i for i in range(len(order))}
        return ''.join(sorted(s, key = lambda x: idxr.get(x, 26)))