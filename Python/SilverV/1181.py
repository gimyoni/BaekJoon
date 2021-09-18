N  = int(input())

words = []

for i in range(N):
    word = input()
    
    if (len(word), word) not in words:
        words.append((len(word), word))
        
# 길이가 짧은 경우 앞으로, 단어의 사전순으로 정렬
answer = sorted(words, key=lambda x: (x[0], x[1])) 

for a in answer:
    print(a[1])
