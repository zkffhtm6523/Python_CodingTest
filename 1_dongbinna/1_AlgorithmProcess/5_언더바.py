# 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용

# 코드 1 : 1~9까지 자연수 합산
summary = 0
for i in range(1, 10):
    summary += i
print(summary)

# 코드 2 : Hello World를 5번 출력
# 변수값이 사용되지 않고, 단순 반복하고자 할 때
for _ in range(5):
    print("Hello World")

# append() : 리스트에 원소 하나 삽입 / O(1)
# sort() : 오름차순 정렬 / O(NlogN)
# sort(reverse = True) : 내림차순 정렬 / O(NlogN)
# reversed() : 리스트의 원소 순서를 모두 뒤집어놓는다. / O(N)
# insert() : 특정한 인덱스에 원소 삽입 / O(N)
# count() : 리스트에서 특정한 값을 가지는 데이터 개수 / O(N)
# remove() : 특정한 값을 갖은 원소 제거, 값이 여러 개면 하나만 제거 / O(N)

# 리스트에서 특정 값을 가지는 원소를 모두 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)