# P.149 음료수 얼려 먹기
# 구멍이 뚫려있는 부분은 0으로, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결되어있는것으로 간주
# 얼음 틀의 모양이 주어졌을때 생성되는 총 아이스크림의 개수를 구하시오
# 첫번째 줄에 얼음틀의 세로길이 N과 가로길이 M (1<=n,m <=1000)
# 두번째 줄 부터 n+1줄까지 얼음틀의 형태가 주어짐
n, m = map(int, input().split())
map = [list(map(int, input())) for _ in range(n)]
cnt = 0

def dfs(x, y):
    if not (0 <= x <= n - 1 and 0 <= y <= m - 1):
        return False
    elif map[x][y] == 0:
        map[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

for i in range(n):
    for k in range(m):
        if dfs(i, k):
            cnt += 1
print(cnt)
