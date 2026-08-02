class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        for cnt, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(pq, (cnt, char))
        s = ""

        while pq:
            count, char = heapq.heappop(pq)
            if len(s) > 1 and s[-1] == s[-2] == char:
                if not pq:
                    break

                count_n, char_n = heapq.heappop(pq)
                s += char_n
                count_n += 1
                if count_n:
                    heapq.heappush(pq, (count_n, char_n))
                heapq.heappush(pq, (count, char))
            else:
                s += char
                count += 1
                if count:
                    heapq.heappush(pq, (count, char))
        

        return s

