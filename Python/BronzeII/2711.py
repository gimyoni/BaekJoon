for _ in range(int(input())):
  n, str = input().split()
  n = int(n)
  print(str[:n-1]+str[n:])
