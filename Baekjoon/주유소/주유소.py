import sys
a = int(input())
road = list(map(int, input().split()))
money = list(map(int, input().split()))

min_money = sys.maxsize # 최솟값과 비교할거기 때문에 최대값을 지정해둠
sum_money = 0
for i in range(len(road)):
  if money[i] < min_money:
    min_money = money[i] # 이전 도시의 최솟값과 비교
  sum_money += min_money * road[i]
print(sum_money)