n = int(input())
x = list(map(int, input().split()))
y = list(sorted(set(x)))
y = {y[i]:i for i in range(len(y))} # dict 형식을 사용

print(*[y[i] for i in x])   # *의 의미 : 리스트의 원소만 출력하고자 함