n = int(input())
m = 0
for i in range(1, n+1):
  a = list(map(int,str(i)))
  m = i + sum(a)
  if m == n:
    print(i)
    break
  if i == n:
    print(0)