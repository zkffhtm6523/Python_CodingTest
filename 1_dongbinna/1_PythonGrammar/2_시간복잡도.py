# 시간 복잡도 계산해보기

# 시간 복잡도 : O(N)
array = [3, 5, 1, 2, 4] # 5개의 데이터 (N = 5)
summary = 0 # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

# 결과를 출력
print('시간 복잡도 : O(N)')
print('결과 : {}'.format(summary))

# 수행 시간은 데이터의 개수 N에 비례할 것임을 예측

# 시간 복잡도 : O(N^2)
array = [3, 5, 1, 2, 4] # 5개의 데이터 (N = 5)

print('\n시간 복잡도 : O(N^2)')
for i in array:
    for j in array:
        temp = i * j
        print('결과 : {}'.format(temp))

# 참고로 모든 2중 반복문의 시간복잡도가 O(N^2)인 것은 아님
# 소스코드가 내부적으로 다른 함수를 호출한다면 그 함수의 사간 복잡도까지 고려 필요하다