for _ in range(3):
  num = list(input())
  arr = [num[0]]
  answer = [1]
  cnt = 1
  for i in range(1, 8):
    if(arr[len(arr)-1]==num[i]):
      cnt += 1
    else:
      arr.append(num[i])
      answer.append(cnt)
      cnt = 1
  answer.append(cnt)
  print(max(answer))
