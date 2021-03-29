# 람다 표현식 : 특정한 기능을 수행하는 함수를 한 줄에 작성 가능
# -> 이름없는 함수로도 불린다.

def add(a, b):
    return a + b


# 일반적인 add() 메서드 사용
print(f"sum[함수] : {add(3, 7)}")

# 람다 표현식으로 구현한 add() 메서드
print(f"sum[람다] : {(lambda a, b: a + b)(3, 7)}")

# 람다, lambda 입력 매개 변수: return 값)(매개 변수)

# 람다 표현식 예시 : 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# 그 튜플의 두 번째 원소
def my_key(x):
    return x[1]

# 정렬 기준은 key 기준
print((sorted(array, key=my_key)))
print((sorted(array, key=lambda x: x[1])))

# 람다 표현식 예시 : 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))