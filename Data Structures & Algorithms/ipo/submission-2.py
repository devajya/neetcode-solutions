class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        combined = [(-p, c) for p, c in zip(profits, capital)]
        combined.sort(key=lambda x: x[1])


        heap = []
        total_cap = w
        i = 0 

        while k > 0:
            while i <len(combined) and combined[i][1] <= total_cap:
                heapq.heappush(heap, combined[i])
                i+=1

            if not heap:
                break
            item = heapq.heappop(heap)
            total_cap += -item[0]
            k-=1

            # print("Combined:", combined, "i: ", i)
            # print("Heap: ", heap)
            # print("item:",item, "cap:", total_cap, "k:", k, "\n")


        return total_cap