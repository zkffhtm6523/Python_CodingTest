# 순열과 조합

# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것

# 순열
from itertools import permutations
# 조합
from itertools import combinations
# 중복 순열
from itertools import product
# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

print(f'순열 : {list(permutations(data, 3))}')
print(f'조합 : {list(combinations(data, 3))}')
# 중복 순열 : 2개를 뽑는 모든 순열 구하기
print(f'조합 : {list(product(data, repeat=2))}')
# 중복 조합 : 2개를 뽑는 모든 조합 구하기
print(f'중복 조합 : {list(combinations_with_replacement(data, 2))}')
