str = input()
result = []
for i in range(len(str)):
  result.append(str[i:])
for i in sorted(result):
  print(i)
