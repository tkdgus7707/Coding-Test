#### 설탕 배달

------

- [문제](https://www.acmicpc.net/problem/2839)



- 풀이

  우선 n을 3과 5의 배수로 나타낼 수 있는지 확인했다. 만약 가능하다면 모든 경우의 수를 리스트로 저장해 그 중 최솟값을 출력했다. 3과 5의 배수로 나타나지 않으면 -1을 출력했다.  



- 참고 풀이

  이 문제는 설탕의 무게를 나타내는 숫자 N이 입력되면 3 킬로그램과 5 킬로그램으로 된 봉지에 나누어 담아서 가장 적은 수의 봉지 개수를 출력하는 문제이다. 설탕을 나눠 담을 때 정확하게 n이 될 수 없는 경우에는 -1을 출력한다.

  설탕의 봉지 개수를 찾는 코드는 while 반복문을 활용하였다. 5의 배수가 될 때까지 설탕의 무게에서 3씩 빼가는 방식으로 코드를 작성했고 딱 나누어 떨어지지 않을 때는 while - else문을 활용해서 -1을 출력하도록 문제를 풀었다. 