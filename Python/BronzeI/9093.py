T = int(input())

for _ in range(T):
  sentence = input().split()
  str  = ""
  for s in sentence:
    str += s[::-1]+" "
  print(str)
