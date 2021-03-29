# 함수의 종류
# 내장 함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


result = add(3, 7)
print(f"더하기 결과 : {result}")

# global 키워드
a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)