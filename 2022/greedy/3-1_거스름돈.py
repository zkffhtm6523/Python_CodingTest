# 거스름돈

n = 1260
count = 0

# 큰 단위 부터 화폐 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n
    n %= coin  # 500으로 나눈 나머지 값
    print('n : ', n)

print(count)
