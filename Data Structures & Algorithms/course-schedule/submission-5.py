class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependants = set()
        visited = set()
        courseMap = {i:[] for i in range(numCourses)}
        for [x, y] in prerequisites:
            courseMap[x].append(y)

        def dfs(course):
            nonlocal dependants
            if course in visited:
                return True
            dependants.add(course)
            for req in courseMap[course]:
                if req in dependants:
                    return False
                if dfs(req) == False:
                    return False
            dependants.remove(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
       



        