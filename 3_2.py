# P.92 큰수의 법칙
# 확률에서 쓰이는 큰수의 법칙과는 다르게 이 문제에서는 다양한 수로 이루어진 배열이 있을 때 주어진 수들을
# M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다

# 예시로 2, 4, 5, 4, 6으로 이루어진 배열이 있을때 M이 8이고 K는 3이라면
# K가 3이기때문에 특정한 수는 최대 3번까지만 더해질 수 있다.
# 따라서 6+6+6+5+6+6+6+5 = 46

# 입력조건 : 첫째줄에 N(2<= N <= 1000), M(1<= M <= 1000), K(1<= K <=10000)의 자연수가 주어지며 공백으로 구분함
# 둘째줄에 N개의 자연수가 주어지고, 각각의 자연수는 1이상 10000이하의 수로 주어진다
# 입력으로 주어지는 K는 항상 M보다 작거나 같다
n, m, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
first = num[n - 1]
second = num[n - 2]
result = 0
temp1 = int(m / (k + 1))
temp2 = m % (k + 1)
result += temp1 * (k * first + second)
result += temp2 * first
print(result)
