import itertools
n, m = map(int, input().split())
num = [x for x in range(1,n+1)]
a = list(itertools.permutations(num,m))
for i in a:
    print(*i)