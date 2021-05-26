N = int(input()) # 문장의 수
for _ in range(N): # 문장의 수만큼 반복
  str = input().split(' ') # 공백을 기준으로 배열 생성
  for i in range(2, len(str)): # 배열 두번째 자리부터
    print(str[i], end=' ') # 줄바꿈 방지
  print(str[0],str[1]) # 배열 첫번째자리까지 문장에 더해주기
