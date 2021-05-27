N = int(input()) # 문장의 수
for _ in range(N): # 문장의 수만큼 반복
  str = input()
  print(str[0]+str[len(str)-1])
