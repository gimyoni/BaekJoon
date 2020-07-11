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



## 8393  : 합

n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

```python
a = int(input())
sum =0
for i in range(1,a+1):
    sum += i
print(sum)
```



## 15552 : 빠른 A+B

본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 `cin`/`cout`을 사용하고자 한다면, `cin.tie(NULL)`과 `sync_with_stdio(false)`를 둘 다 적용해 주고, `endl` 대신 개행문자(`\n`)를 쓰자. 단, 이렇게 하면 더 이상 `scanf`/`printf`/`puts`/`getchar`/`putchar` 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, `Scanner`와 `System.out.println` 대신 `BufferedReader`와 `BufferedWriter`를 사용할 수 있다. `BufferedWriter.flush`는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, `input` 대신 `sys.stdin.readline`을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 `.rstrip()`을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

자세한 설명 및 다른 언어의 경우는 [이 글](http://www.acmicpc.net/board/view/22716)에 설명되어 있다.

[이 블로그 글](http://www.acmicpc.net/blog/view/55)에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.

```python
import sys

a = int(input())

for i in range(a):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
```



## 2741  : N 찍기 

자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
a = int(input())

for i in range(1,a+1):
    print(i)
```



## 2742 : 기찍 N

자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
a = int(input())

for i in range(0,a):
    print(a-i)
```



## 11021 : A+B-7

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
a = int(input())

for i in range(1,a+1):
    b,c = map(int, input().split())
    print("Case #%d"%int(i)+":",(b+c))
```



## 11022  : A+B-8

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
a = int(input())

for i in range(1,a+1):
    b,c = map(int, input().split())
    print("Case #%d: %d + %d = %d"%(int(i),b,c,(b+c)))
```



## 2438 : 별 찍기-1 

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

```python
a = int(input())

for i in range(1,a+1):
    print("*"*i)
```



## 2439 : 별 찍기 - 2

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

```python
a = int(input())

for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)
  
```

