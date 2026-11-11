class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(numCourses)}

        for n1,n2 in prerequisites:
            adj[n1].append(n2)
        
        output = []
        visit,cycle = set(),set()
        
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            for j in adj[i]:
                if dfs(j) is False:
                    return False
            cycle.remove(i)
            visit.add(i)
            output.append(i)
            return True

        for cource in range(numCourses):
            if dfs(cource) is False:
                return []
        return output