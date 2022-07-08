# P.96 숫자 카드 게임
# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
# 입력조건 : 첫번째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다(1<=N, M<=100)
# 둘째 줄에서부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10000이하의 자연수이다.

n, m = map(int, input().split())
data = []
for i in range(n):
    num = list(map(int, input().split()))
    data.append(min(num))
print(max(data))
