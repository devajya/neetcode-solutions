class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        top = []

        adj_list = defaultdict(list)
        in_degree = [0]*numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        q = deque()
        for course, in_d in enumerate(in_degree):
            if in_d == 0:
                q.append(course)

        while q:
            level_count = len(q)
            for _ in range(level_count):
                course = q.popleft()
                top.append(course)
                for available in adj_list[course]:
                    in_degree[available] -= 1
                    if in_degree[available] == 0:
                        q.append(available)

        
        return top if len(top) == numCourses else []