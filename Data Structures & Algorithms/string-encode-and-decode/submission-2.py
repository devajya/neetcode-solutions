class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "@" + s
        print(encoded)
        return encoded
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "@":
                num += s[i]
                i+=1
                continue
            length = int(num)
            decoded.append(s[i+1: i+length+1])
            i = i+length+1
        
        print(decoded)

        return decoded
            