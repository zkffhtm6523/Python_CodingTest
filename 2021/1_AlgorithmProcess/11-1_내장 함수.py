# 내장 함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수

# itertools : 반복되는 형태 데이터 처리
#  : 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용됨

# heapq : 힙(Heap) 자료구조를 제공
#  : 일반적으로 우선순위 큐 기능을 구현하기 위해 사용

# bisect : 이진 탐색 기능 제공
# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
# math : 필수적인 수학적 기능 제공
#  : 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이(pi)와 같은 상수 포함

# sum()
print(f'sum : {sum([1, 2, 3, 4, 5])}')

# min()
print(f'min : {min(7, 3, 5, 2)}')
# max()
print(f'max : {max(7, 3, 5, 2)}')

# eval() : 하나의 식이 있을 때 결과를 수 형태로 반환
print(f"eval : {eval('(3+5)*7')}")

# sorted()
print(f"오름차순 : {sorted([9, 1, 8, 5, 4])}")
print(f"내림차순 : {sorted([9, 1, 8, 5, 4], reverse=True)}")

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(f"내림차순 람다 : {result}")