nums = []
for i in range(10):
  num = int(input())
  n = num%42
  nums.append(n)

result = set(nums)
print(len(result))
