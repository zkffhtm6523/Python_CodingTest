n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때 까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k


result += (n - 1)
print(result)
