# Counter : 등장 횟수를 세는 기능 제공

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

# blue 등장 횟수
print(counter['blue'])
# green 등장 횟수
print(counter['green'])
# 사전 자료형으로 반환
print(dict(counter))