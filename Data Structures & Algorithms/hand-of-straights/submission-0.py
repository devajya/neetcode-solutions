class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        maps = defaultdict(int)
        for h in hand:
            maps[h] += 1

        hand.sort()

        for h in hand:
            if maps[h] > 0:
                for target in range(h, h+groupSize):
                    if not maps[target]:
                        return False
                    else:
                        maps[target] -= 1
        return True