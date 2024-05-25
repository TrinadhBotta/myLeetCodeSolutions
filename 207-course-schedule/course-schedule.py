class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


        def isCyclicUtil(v, visited, recStack):
            visited.add(v)
            recStack.add(v)

            if v not in adj:
                recStack.remove(v)
                return False

            for prerequisite in adj[v]:
                if prerequisite not in visited:
                    if isCyclicUtil(prerequisite, visited, recStack):
                        return True
                elif prerequisite in recStack:
                    return True
    
            recStack.remove(v)
            return False


        adj = {}
        for i in prerequisites:
            adj[i[1]] = adj.get(i[1],[]) + [i[0]]
        
        visited = set()
        recStack = set()

        for subject in adj:
            if subject not in visited:
                if isCyclicUtil(subject, visited, recStack) == True:
                    return False
        return True