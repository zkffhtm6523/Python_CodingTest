# 카드 게임

# 가로 * 세로 입력
n, m = map(int, input().split())

result = 0

# 각 행마다 카드 번호 입
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    result = max(result, min_value)

print('결과 : {}'.format(result))
