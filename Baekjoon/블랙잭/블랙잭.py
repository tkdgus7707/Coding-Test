n, m = map(int, input().split())
card = list(map(int, input().split()))

from itertools import combinations # 조합을 찾기위해

card_sum = list(set(map(sum, combinations(card, 3)))) # 3개의 조합들의 합을 찾음
card_sum.sort(reverse=True) # 역순으로 정렬
for i in card_sum:
  if m-i >= 0: # m을 넘지 않는 합이 나올때까지 찾음
    print(i) # 제일먼저 나온 합을 출력
    break