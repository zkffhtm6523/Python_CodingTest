# 파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)로 지정
# 조건문의 기본적인 형태는 if ~ elif ~ else

score = 85

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
else:
    print("학점 : F")

# 논리 연산자(Java는 && || !등
# X and Y
# X or Y
# not X

# 파이썬의 기타 연산자
# in 연산자와 not in 연산자
# x in list : 리스트 안에 x가 들어있을 때 True
# x not in list : 리스트 안에 x가 들어있지 않을 때 True

# Pass : 아무것도 처리하고 싶지 않을 때 pass
# 나중에 소스코드 적고 싶을 때

if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 파이썬 조건문 내에서의 부등식
x = 15
if 0 < x < 20:
    print('x는 0 이상 20 미만의 수입니다.')
