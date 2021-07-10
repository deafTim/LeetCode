class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [0,1,0,-1,0]
        m,n = len(maze), len(maze[0])
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = 0
        # building length to exit
        while q:
            y0, x0 = q.popleft()
            for i in range(4):
                y, x = y0+dirs[i], x0+dirs[i+1]
                if 0<=y and y<m and 0<=x and x<n and maze[y][x]!='+':
                    if maze[y][x] == '.':
                        maze[y][x] = maze[y0][x0]+1
                        q.append([y,x])
                    elif maze[y][x] > maze[y0][x0]+1:
                        maze[y][x] = maze[y0][x0]+1
                        q.append([y,x])
        mn = 10000
        m,n = n,m
        # checking edges of the maze
        for i in range(n):
            left, right = maze[i][0], maze[i][m-1]
            if left!='+' and left!='.' and [i,0]!=entrance:
                mn = min(left, mn)
            if right!='+' and right!='.' and [i,m-1]!=entrance:
                mn = min(right, mn)
        for i in range(m):
            top, bottom = maze[0][i], maze[n-1][i]
            if top!='+' and top!='.' and [0,i]!=entrance:
                mn = min(top, mn)
            if bottom!='+'  and bottom!='.' and [n-1,i]!=entrance:
                mn = min(bottom, mn)
        if mn==10000:
            return -1
        return mn

