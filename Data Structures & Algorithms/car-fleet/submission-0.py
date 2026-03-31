class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = [(p, s) for p,s in zip(position, speed)]
        temp.sort(reverse=True)

        ans = 0
        prevTime = -1
        for i,car in enumerate(temp):
            time = (target-car[0]) / car[1]
            if time > prevTime:
                ans+=1
                prevTime = time
        
        return ans