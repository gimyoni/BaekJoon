# 줄의 수
N = int(input())
# 줄의 수만큼 반복
for _ in range(N):
  s = input() # 단어 입력
  print(s[0].upper()+s[1:]) # 첫글자만 대문자로
