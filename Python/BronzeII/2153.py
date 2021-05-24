word = input()
sum = 0
for w in word:
  if w.islower(): sum+=ord(w)-96
  else: sum+=ord(w)-64

chk = 0
for i in range(2, sum):
  if sum % i == 0:
    print("It is not a prime word.")
    chk += 1
    break
  
if(chk==0): print("It is a prime word.")
