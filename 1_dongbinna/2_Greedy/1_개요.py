# 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 문제를 풀기위한 최소한의 아이디어 필요
# 정당성 분석 필요, 최적의 해

# 문제 상황) 루트 노드부터 시작하여 거쳐가는 노드 값의 합을 최대로 만드는 해
# 문제 상황) 루트 노드부터 시작하여 매 상황에서 가장 큰 값만 고른다면?

# 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많다
# 최적의 해를 얻을 수 있다는 것을 추론할 수 있어야 함

# 문제) 거스름 돈 : 문제 설명
# 당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리
# 동전이 무한히 존재한다고 가정합니다. 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의
# 최소 개수를 구하세요. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.

# 문제) 거스름 돈 : 아이디어
# 가장 큰 화폐 단위부터 돈을 거슬러주면 됨
# N = 1,260원

# 문제) 거스름 돈 : 정당성 분석
# 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유
#     가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해
#     다른 해가 나올 수 없기 때문
# 만약 800원을 거슬러 주어야 하는데 화폐 단위가 500원, 400원, 100원이라면 어떻게 될까요?
# 큰 단위가 작은 단위의 배수가 아니라면, 정당성 분석 보장 못함

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
print(1260 / 500)
print(1260 // 500)
print(1260 % 500)

for coin in array:
    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    # n을 coin으로 나눈 몫을 count에 담기
    count += n // coin
    # n에 나머지 260 담기
    n %= coin

# 문제) 거스름 돈 : 시간 복잡도 분석
# 화폐의 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K)

print(count)