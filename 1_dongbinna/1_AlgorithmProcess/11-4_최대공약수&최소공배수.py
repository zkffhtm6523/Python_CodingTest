import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(f"최대 공약수 : {math.gcd(21, 14)}")
print(f"최소 공배수 : {lcm(21, 14)}")