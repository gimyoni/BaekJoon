num = int(input())
h = 0

for n in range(1, num+1):
    if n <= 99: 
        h += 1 
    else:     
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            h+=1
print(h)
