class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        s = set(deadends)
        if "0000" in s:
            return -1
        s.add("0000")


        def adjacent(code: str):
            ans = []
            for i in range(len(code)):
                added = str((int(code[i])+1)%10)
                ans.append(code[:i] + added + code[i+1:])

                subtracted = str((int(code[i])-1+10)%10)
                ans.append(code[:i] + subtracted + code[i+1:])
            return ans
        
        q = deque([("0000", 0)])
        while q:
            code, count = q.popleft()
            if code == target:
                return count
            for new_code in adjacent(code):
                if new_code not in s:
                    s.add(new_code)
                    q.append((new_code, count+1))
            
        return -1

    
