n = int(input())
num = 0
count = 0
while 1:
    num += 1
    if '666' in str(num): # num에 666이 있을때마다 count 1 증가
        count += 1
        if count == n: # count가 입력받은 수와 같아지면 num을 출력
            print(num)
            break