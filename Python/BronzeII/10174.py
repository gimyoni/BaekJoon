n = int(input())
for _ in range(n):
  str = input().upper()
  if(str==str[::-1]): print("Yes")
  else: print("No")
