class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        in_degree = [0]*numCourses
        ans = [set() for _ in range(numCourses)]
        for p, q in prerequisites:
            adj[p].add(q)
            in_degree[q] += 1

        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])


        while q:
            crs = q.popleft()
            for nei in adj[crs]:
                ans[nei].add(crs)
                ans[nei].update(ans[crs])
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return [u in ans[v] for u, v in queries]