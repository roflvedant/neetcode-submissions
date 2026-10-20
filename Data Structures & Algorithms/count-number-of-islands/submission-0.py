class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()

        count = 0

        row = len(grid)
        col = len(grid[0])


        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            dir = [[1,0],[-1,0],[0,1],[0,-1]]

            while q:
                r, c = q.popleft()

                for dr, dc in dir:
                    if (r + dr) in range(row) and (c + dc) in range(col) and grid[r + dr][c + dc] == "1" and not ((r+dr),(c+dc)) in visited:
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        return count