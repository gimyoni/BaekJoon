import sys
while True: 
  str = sys.stdin.readline().rstrip('\n') 
  up, low, space, num = 0, 0, 0, 0 
  if not str:
    break
  for s in str:
    if s.isspace():
      space += 1
    elif s.islower():
      low += 1
    elif s.isupper():
      up += 1
    else: 
      num += 1
  print(low,up,num,space)
