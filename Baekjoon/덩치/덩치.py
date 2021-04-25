n = int(input())
people = list()
for _ in range(n):
    m = list(map(int, input().split()))
    people.append(m)

for i in people: # 모든 사람과 비교하여 키 몸무게가 다 작을때 rank가 1 증가
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')