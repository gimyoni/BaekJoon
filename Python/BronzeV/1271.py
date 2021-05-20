n, m = map(int, input().split()) // 공백을 기준으로 나누어 입력받기

give = n//m // 생명체 하나에게 돌아가는 돈의 양
spare = n%m // 1원씩 분배할 수 없는 남는 돈

print(give)
print(spare) // 출력
