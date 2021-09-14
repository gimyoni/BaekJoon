N = int(input())

cnt = 0

while True:
    if(N % 5 == 0): # 5킬로그램을 들고갈 수 있다면
      cnt = cnt + (N // 5) # 나눈 몫과 cnt를 더함
      print(cnt)
      break

    N -= 3 # 3킬로그램 봉지를 들고감
    cnt += 1 # 개수를 더해줌
    
    if (N < 0): # 정확하게 N킬로그램을 만들수 없다면
      print(-1) # -1을 출력
      break
