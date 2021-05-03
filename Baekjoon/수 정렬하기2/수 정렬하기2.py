import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
    # [sys.stdin.readline().strip() for i in range(n)]
for i in sorted(l):
    # sys.stdout.write(str(i)+'\n')
    print(i)
