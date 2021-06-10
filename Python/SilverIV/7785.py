N = int(input())
p = {}

for _ in range(N):
  n, c = input().split()

  if c == "enter":
    p[n] = "enter"
  else:
    if p[n]:
      del p[n]

for people in sorted(p, reverse=True):
  print(people)
