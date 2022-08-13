# P.217 1로 만들기
# 정수x가 주어질때 사용가능한 연산은 4가지이다.
# 1. x가 5로 나누어떨어지면 5로 나눈다
# 2. x가 3으로 나누어떨어지면 3으로 나눈다
# 3. x가 2로 나누어떨어지면 2로 나눈다
# 4. x에서 1을 뺀다
# 정수 x가 주어졌을때 연산4개를 적절히 사용해서 1을 만들때 연산을 사용하는 최소값을 출력

n = int(input())

def make1_hong(num):
    cnt = 0
    d = [0] * (num + 1)
    d[0] = 999
    d[1] = 1
    for i in range(2, num + 1):
        arr = []
        arr.clear()
        if i % 2 == 0:
            arr.append(i // 2)
        if i % 3 == 0:
            arr.append(i // 3)
        if i % 5 == 0:
            arr.append(i // 5)
        arr.append(i - 1)
        brr = []
        brr.clear()
        for a in arr:
            brr.append(d[a])
            mini = min(brr)
            if d[a]==mini:
                d[i]=a
    #     print('i :',i,"   후보군 :",arr)
    # print(d)
    x=num
    while x!=1:
        x=d[x]
        cnt+=1

    return cnt

def make1_book(x):
    d = [0] * 30000
    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[x]

print(make1_hong(n))