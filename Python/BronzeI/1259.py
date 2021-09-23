while True:
  n = input()

  if n=='0': # 0을 입력받으면 while문을 벗어남
    break
  
  if n[::-1] == n: # 팰린드롬수이면
      print('yes')
  else:
      print('no')
