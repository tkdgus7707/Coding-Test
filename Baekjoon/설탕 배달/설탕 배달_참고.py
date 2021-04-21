n = int(input())
bag = 0
while n >= 0:
  if n % 5 == 0: # 5의 배수이면 출력
    bag += n//5
    print(bag)
    break
  n -= 3 # 5의 배수가 아니면 3을 계속 빼줌
  bag += 1
else: # 나누어떨어지지 않으면 -1 출력
  print(-1)