N = int(input())
for _ in range(N):
  r = input()
  r_len = len(r)//2
  if(r[r_len-1]==r[r_len]):
    print("Do-it")
  else:
    print("Do-it-Not")
