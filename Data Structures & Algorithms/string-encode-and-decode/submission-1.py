class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        seps = [str(len(st))+"#" for st in strs]
        for st, sep in zip(strs, seps):
            temp.append(sep)
            temp.append(st)
        print(temp)
        return ''.join(temp)
    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            l = int(s[i:j])
            i = j+1
            j = i+l
            ans.append(s[i:j])
            i=j

        return ans
