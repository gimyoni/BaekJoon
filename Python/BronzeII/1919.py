from collections import Counter

s1 = Counter(input())
s2 = Counter(input())

print(sum((s1-s2).values())+sum((s2-s1).values()))
