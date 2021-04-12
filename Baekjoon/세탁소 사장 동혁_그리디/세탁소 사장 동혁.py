num = int(input())

money = [25, 10, 5, 1]
for _ in range(num):
    coin = int(input())
    for i in money:
        print(coin // i , end=' ')
        coin %= i