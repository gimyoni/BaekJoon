[toc]

# for문

## 2739  : 구구단

N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

```python
a = int(input())

for i in range(1,9+1):
    print(a,"*",i,"=",a*i)
```



## 10950 : A+B - 3

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
a = int(input())

for i in range(0,a):
    b, c = map(int,input().split())
    print(b+c)
```

