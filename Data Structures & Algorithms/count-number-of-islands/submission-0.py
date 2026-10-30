class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visit = set()
        island = 0
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                r, c = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    row = r+dr
                    col = c +dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) 
                    and grid[row][col] == "1" and (row,col) not in visit):
                        queue.append((row,col))
                        visit.add((row,col))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island +=1
        return island