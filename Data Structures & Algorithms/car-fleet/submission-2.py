class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vels = [(p, s) for p, s in zip(position, speed)]
        vels.sort(reverse = True)

        times = [(target-p)/s for p, s in vels]
        stack = []

        for t in times:
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return  len(stack)