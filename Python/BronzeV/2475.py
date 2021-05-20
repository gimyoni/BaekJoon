nums = list(map(int,input().split())) // 5자리수 배열에 넣기
sum = 0 // 제곱한 수의 합을 저장할 sum 초기화
for n in nums: // 숫자 하나씩 가져오기
  sum += pow(n,2) // 제곱한 수 sum에 더하기
print(str(sum)[-1]) // 숫자를 문자열로 변경해 마지막 자리수 슬라이싱 하기
