class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visit = set()

        row = len(grid)
        col = len(grid[0])

        count = 0

        def bfs(r,c):
            q = deque([(r,c)])
            visit.add((r,c))
            dir = [[-1,0],[1,0],[0,1],[0,-1]]


            while q:
                r, c = q.popleft()
                for dr, dc in dir:
                    newR = r + dr
                    newC = c + dc
                    if newR in range(row) and newC in range(col) and grid[newR][newC] == "1" and (newR,newC) not in visit:
                        q.append((newR,newC))
                        visit.add((newR,newC))



        for r in range(row):
            for c in range(col):

                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    count += 1
        return count
