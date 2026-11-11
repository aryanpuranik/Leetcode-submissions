class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}

        for n1,n2 in prerequisites:
            adj[n1].append(n2)
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            if adj[i] == []:
                return True
            visit.add(i)

            for j in adj[i]:    
                if dfs(j) is False:
                    return False
            visit.remove(i)
            adj[i] = []
            return True
        

        for cource in range(numCourses):
            if dfs(cource) is False:
                return False
        return True
        