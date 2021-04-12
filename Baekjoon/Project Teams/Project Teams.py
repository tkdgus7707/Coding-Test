import sys

num = int(input())
coding = list(map(int, input().split()))
coding.sort()

min_w = sys.maxsize
for i in range(num):
    w = coding[i] + coding[-i-1]
    min_w = min(min_w,w)
print(min_w)