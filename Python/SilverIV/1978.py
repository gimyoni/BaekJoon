n = int(input())
nums = list(map(int, input().split()))
num_cnt =0
for i in nums:
  cnt = 0
  if i == 0:
    continue
  for j in range(2, i+1):
    if i%j == 0:
      cnt+=1
  if(cnt == 1):
    num_cnt +=1
print(num_cnt)
