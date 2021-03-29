# input() 함수는 한 줄의 문자열을 입력 받는 함수
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 예시) 공백을 기준으로 구분뒨 데이터를 입력받을 때
#     - list(map(int, input().split()))

# 예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면(입력 데이터가 4개 이상이면 안 됨)
#      - a, b, c = map(int, input().split())

# data = input().split()

# print(data)

# 빠르게 입력 받기
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드 이용
# 단, 입력 후 엔터(Enter)가 줄바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용

# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# print()는 기본적으로 출력 이후 줄바꿈 수행
#     - 줄바꿈을 원치않는 경우 'end'속성을 이용할 수 있음

print(7, end = " ")
print()
# f-string
answer = 7
print(f"정답은 {answer}입니다.")