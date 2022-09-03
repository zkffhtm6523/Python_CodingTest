# N, M, K를 공백으로 구분하여 입력받기

n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째 큰 수

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)



