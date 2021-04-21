n = int(input())
count = list()

# 5와 3의 배수로 n을 만들 수 있는지 확인
for i in range((n//5) + 1):
  k = n - 5*i
  if k % 3 == 0:
    count.append(i + (k//3)) # 모든 경우의 수를 리스트의 저장
if count == []:
  print(-1) # 3, 5의 배수로 n을 만들 수 없으면 -1 출력
else:
  print(min(count)) # 만들어진 조합중에서 최소 봉지 개수를 선택