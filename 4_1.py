# P.110 상하좌우
# 여행가 A는 N x N 크기의 정사각형 공간에 있음( 1x1 크기의 정사각형으로 나누어짐)
# 좌상단 1,1    우하단 N,N
# 여행가는 상,하,좌,우 방향으로 이동가능하며 시작좌표는 항상 1,1
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있음
n = int(input())
dir = list(input().split())
x = 1
y = 1
# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for d in dir:
    if d == "L":
        if not (x + dx[0] < 1):
            y += dy[0]
    if d == "R":
        if not (x + dx[1] > n):
            y += dy[1]
    if d == "U":
        if not (x + dx[2] < 1):
            x += dx[2]
    if d == "D":
        if not (x + dx[3] > n):
            x += dx[3]
print(x, y)
