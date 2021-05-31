from collections import Counter

t = int(input())
for _ in range(t):
  n = int(input())
  clothes = {}
  for _ in range(n):
    name, kind = input().split()
    if kind in clothes:
      clothes[kind] += 1
    else:
      clothes[kind] = 1
  cnt = 1
  for key in clothes:
    cnt *= (clothes[key]+1)
  print(cnt-1) 
