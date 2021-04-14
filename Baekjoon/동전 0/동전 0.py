num, money = map(int, input().split())
change = list()
count = 0

for _ in range(num):
    a = int(input())
    change.append(a)

for i in range(-1,-(num+1),-1):
    count += money // change[i]
    money = money % change[i]
    if money == 0:
        break
print(count)