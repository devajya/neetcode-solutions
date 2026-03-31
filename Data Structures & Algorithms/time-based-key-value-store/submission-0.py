class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keys = self.store.get(key)
        
        ret = ""

        if not keys:
            return ret

        l=0
        r=len(keys)-1

        while l<=r:
            m = (l+r)//2

            if keys[m][0] <= timestamp:
                ret = keys[m][1]
                l=m+1
            else:
                r = m-1

        return ret


