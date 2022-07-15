# P.197 부품 찾기
# n개의 부품은 정수형태의 고유번호가 부여됨, 손님이 m개 종류의 부품을 대량구매할때 가게안에 부품이 모두 있는지 확인하는 견적서 프로그램
# 첫째줄에 정수 n이 주어지고, 둘째줄에 공백으로 구분하여 n개의 정수가 주어짐
# 셋째줄에 정수 m이 주어지고, 넷쨰줄에 공백으로 구분하여 m개의 정수가 주어짐
n = int(input())
parts_shop = list(map(int, input().split()))
m = int(input())
parts_client = list(map(int, input().split()))

parts_shop.sort()

start=0
end=n-1
def parts_sort(start, end, shop, client):
    while start<=end:
        mid = (start + end) // 2
        if shop[mid] == client:
            return True
        elif shop[mid] > client:
            start = shop[mid]
        elif shop[mid] < client:
            end = shop[mid]
        else:
            return False

for i in parts_client:
    if parts_sort(start, end, parts_shop, i):
        print("yes", end=' ')
    else:
        print("no", end=' ')

