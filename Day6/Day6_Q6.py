#rat and maze

def maze(grid,path,i,j,n):
    if i==n and j==n:
        print(path)
        return
    if i+1<=n and grid[i+1][j]==1:
        maze(grid,path+'D',i+1,j,n)
    if j+1<=n and grid[i][j+1]==1:
        maze(grid,path+'R',i,j+1,n)

grid=[[1,1,0,1],
     [1,1,0,1],
     [0,1,0,0],
     [1,1,1,1]]

n=len(grid)
maze(grid," ",0,0,n-1)