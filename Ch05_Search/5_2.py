# P.152 미로 탈출
# n X m 크기의 직사각형 형태의 미로에 갇혀있음. 위치는 1,1 이고 미로의 출구는 (n,m)에 위치하며 한번에 한칸씩 이동 가능
# 괴물이 있는부분은 0으로 없는부분은 1로 표현되어있음 이때 탈출하기위해 움직여야한느 최소칸의 개수는?
# 처음칸과 마지막칸 모두를 포함하여 셈
from collections import deque
n, m = map(int, input().split())
map = [list(map(int, input())) for _ in range(n)]
a, b = 0, 0
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(map, a, b):
    cnt = 0
    queue = deque()
    queue.append([a, b, cnt])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        dot = queue.popleft()
        x = dot[0]
        y = dot[1]
        cnt = dot[2]
        cnt += 1
        visited[x][y] = True
        if x == n - 1 and y == m - 1:
            print("x:", x, "y:", y, "count: ", cnt)
            break
        for i in range(4):
            if (0 <= x + dx[i] < n and 0 <= y + dy[i] < m) and map[x + dx[i]][y + dy[i]] == 1 and not visited[x + dx[i]][y + dy[i]]:
                queue.append([x + dx[i], y + dy[i], cnt])
                print("x:", x, "y:", y, "count: ", cnt)
    return cnt

print(bfs(map, a, b))