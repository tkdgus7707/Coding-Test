n, m = map(int, input().split())

num_list = [1+i for i in range(n)] # 숫자 리스트
check_num = [False]*n     # 중복숫자 체크
arr = list() # 출력할 수열

def dfs(x):
    if x == m:  # 수열 m개를 충족할 경우 출력
        print(*arr)
        return

    for i in range(n):
        if check_num[i]:    # 중복될 경우 패스
            continue

        arr.append(num_list[i]) # 수열 추가
        check_num[i] = True # 사용한 수 체크
        dfs(x+1) # +1번째 수열을 위해 재귀

        arr.pop()   # 수열 마지막 자리 삭제
        check_num[i] = False    #사용한 수 초기화
dfs(0)