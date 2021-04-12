num = int(input())
p = list(map(int, input().split()))
p.sort() # 오름차순으로 정렬

time = 0
min_time = 0
for i in p:
    time += i # 각자 걸린 시간
    min_time += time # 시간들의 합
print(min_time)

# 각자 걸리는 시간을 최소로 하면 합도 최소가 된다.
# 그리디 탐색법