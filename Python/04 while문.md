[toc]

# while문

## 10952 : A+B-5

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
a, b= map(int,input().split())

while(a!=0 and b!=0):
    print(a+b)
    a, b= map(int,input().split())
```

