# 구현이란 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정

# 흔히 알고리즘 대회에서 구현 유형의 문제란 무엇을 의미?
#   풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭

# 구현 유형의 예시는 다음과 같습니다.
#   알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
#   실수 연산을 다루고, 특성 소수점 자리까지 출력해야 하는 문제
#   문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
#   적절한 라이브러리를 찾아서 사용해야 하는 문제

# 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미로 사용됩니다.
print("----------Matrix----------")
for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end=' ')
    print()

print("----------Vector----------")
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)