n = 0
m = 0
graph = []

def ice(mat):
    global n 
    n = len(mat)
    
    global m 
    m = len(mat[0])

    global graph
    graph = mat
    
    result = 0
    
    # 2. 계산
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result = result + 1
    # 3. 반환
    return result


def dfs(x,y):
    # 초기화
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


