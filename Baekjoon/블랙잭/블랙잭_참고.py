n, m = map(int, input().split())
card = list(map(int, input().split()))

from itertools import combinations # 조합을 찾기위해

biggest_sum = 0
for i in combinations(card, 3): # 3개 조합
  temp_sum = sum(i) # 카드 합을 임시저장
  if biggest_sum < temp_sum <= m:
    biggest_sum = temp_sum
print(biggest_sum)