n = int(input())
m = 0
if n < 10: # n이 한자리수면 분해합 할 수 없음
  print(0)
else:
  for i in range(10,n+1):
    for j in str(i):
      m += int(j) # 각 자리수의 합
    if m + i == n: # 분해합을 이룰 때 출력
      print(i)
      break
    else:
      m = 0
  if m == 0:
    print(0)