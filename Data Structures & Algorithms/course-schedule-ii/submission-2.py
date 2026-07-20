class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adj = defaultdict(list)
        in_d = [0]*numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            in_d[c] += 1
        
        q = deque()

        for c, d in enumerate(in_d):
            if d == 0:
                q.append(c)
        
        while q:
            level_count = len(q)
            for _ in range(level_count):
                c = q.popleft()
                ans.append(c)
                for course in adj[c]:
                    in_d[course] -=1
                    if in_d[course] == 0:
                        q.append(course)

        return ans if len(ans) == numCourses else []