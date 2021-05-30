def rev(num): # 숫자를 역순으로 변환하는 함수
  return int(str(num)[::-1])

x, y = map(int, input().split()) #x, y 입력
print(rev(rev(x)+rev(y)))
