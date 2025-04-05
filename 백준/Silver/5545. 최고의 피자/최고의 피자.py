import sys
input = sys.stdin.readline

N = int(input()) # 토핑개수
A, B = map(int, input().split()) # 도우가격, 토핑가격
C = int(input()) # 도우열량
toppings = sorted((int(input()) for _ in range(N)), reverse=True) # 토핑열량

total_kcal = C
total_price = A
max_kcal_per_cost = C/A

for topping in toppings:
    new_total_price = total_price + B
    new_total_kcal = total_kcal + topping
    new_kcal_per_cost = new_total_kcal / new_total_price
    if max_kcal_per_cost < new_kcal_per_cost:
        total_kcal = new_total_kcal
        total_price = new_total_price
        max_kcal_per_cost = new_kcal_per_cost
    else:
        break

print(int(max_kcal_per_cost))