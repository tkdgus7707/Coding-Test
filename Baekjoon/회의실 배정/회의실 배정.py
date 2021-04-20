num = int(input())
time = list()
for _ in range(num):
    a = list(map(int, input().split()))
    time.append(a)

# 끝나는 시간 순으로 정렬을 한 후, 시작 시간 순으로 정렬
time.sort(key = lambda x: (x[1], x[0]))

count = 0
end = 0
for i in time:
    if i[0] >= end: # 이전 종료시간보다 시작시간이 커야함
        end = i[1]
        count += 1

print(count)