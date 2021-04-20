sik = input().split('-') # -로 구분
result = 0

for i in map(int, sik[0].split('+')): # - 앞까지는 다 더해줌
  result += i
for i in sik[1:]: # -가 나온 뒤부터는 다 빼주어야 최솟값
  result -= sum(map(int, i.split('+'))) # +를 다 없애고 합

print(result)