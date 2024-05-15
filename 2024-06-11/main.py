class Solution:
    def addDirections(self, r, c):
        return [(r, c - 1),
                (r, c + 1),
                (r - 1, c),
                (r + 1, c)]

    def bfs(self, grid, r, c, visited, rows, cols):
        queue = self.addDirections(r, c)
        visited.add((r, c))
        while queue:
            current = queue.pop(0)
            r = current[0]
            c = current[1]
            if (c in range(cols) and
                r in range(rows) and
                grid[r][c] and 
                (r, c) not in visited):
                value = grid[r][c]
                visited.add((r, c))
                if value == "1":
                    queue += self.addDirections(r, c)

        return visited

    def numIslands(self, grid: List[List[str]]) -> int:
        # I have visited set with coordinates
        # i iterate through coordinates
        # if its land then find the whole land with bfs and mark visited
        # also keep count of the islands
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                value = grid[r][c]
                if value == "1" and (r, c) not in visited:
                    visited = self.bfs(grid, r, c, visited, rows, cols)
                    islands += 1

        return islands
        