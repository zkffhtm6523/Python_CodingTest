# 1부터 9까지 모든 정수의 합 구하기(While문)

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print('while문 합산 결과 : {}'.format(result))

# 반복문 : for문
array = [9, 8, 7, 6, 5]

for x in array:
    print(x, end=" ")

# for문에서 연속적인 값을 차례대로 순회할 때 range(시작 값, 끝 값 + 1)
# 인자를 하나만 넣으면 자동으로 시작 값은 0
print()
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(f'range & continue 사용 결과 : {result}')

scores = [90, 85, 77, 65, 97]
for i in range(5):
    if scores[i] > 80:
        print(f'{i + 1} 번 학생은 합격입니다')

# 학생들의 합격 여부 판단 예제 2) 특정 번호의 학생은 제외하기
print('-----------2) 특정 번호의 학생은 제외하기-----------')
cheating_student_list = {2, 4}
for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(f'{i + 1}번 학생은 합격입니다.')