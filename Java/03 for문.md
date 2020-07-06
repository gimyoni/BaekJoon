[toc]
# for문

## 2739 :  구구단

구구단을 출력하는 문제

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
	
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i=1; i<=9; i++) {
			System.out.println(num+" * "+i+" = "+num*i);
		}
	}

}
```



## 10950 : A+B - 3

A+B를 여러 번 출력하는 문제

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i =0;i<num; i++) {
			int a = scan.nextInt();
			int b = scan.nextInt();
			
			System.out.println(a+b);
		}
		
		
	}

}
```



## 8393 : 합

1부터 N까지의 합을 구하는 문제. 물론 반복문 없이 풀 수도 있습니다.

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
	
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		int sum=0;
		
		for(int i=1; i<=num; i++) 
		{
			sum+=i;
		}
		
		System.out.println(sum);
	}

}
```



## 15552 : 빠른 A+B

빠르게 입력받고 출력하는 문제

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int num = Integer.parseInt(br.readLine());
		StringTokenizer str;
		
		for(int i =0; i<num; i++){
			
			str = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(str.nextToken());
			int b = Integer.parseInt(str.nextToken());
			
			int sum = a+b;
			
			bw.write(sum+"\n");

		}
		bw.flush();
		bw.close();
		
	}

}
```



## 2741 : N 찍기

자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i =1; i<=num; i++) {
			System.out.println(i);
		}
		
	}

}
```



## 2742 : 기찍 N

자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i = num; i>=1; i--) {
			System.out.println(i);
		}
		
	}

}
```



## 11021 : A+B-7

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i =1; i<=num; i++) {
		
			int a = scan.nextInt();
			int b = scan.nextInt();
			
			System.out.println("Case #"+i+": "+(a+b));
		}		
	}

}
```



## 11022 : A+B-8

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i =1; i<=num; i++) {
		
			int a = scan.nextInt();
			int b = scan.nextInt();
			
			System.out.println("Case #"+i+": "+a+" + "+b+" = "+(a+b));
		}		
	}

}
```



## 2438 : 별 찍기 -1

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i = 1; i<=num; i++) {
			for(int j =1; j<=i; j++) {
				System.out.print("*");
			}
			System.out.println("");
		}		
	}

}
```



##  2439 : 별 찍기 -2

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

```java
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		for(int i = 1; i<=num; i++) {
			for(int j =num-1; j>=i; j--) {
				System.out.print(" ");
			}
			for(int k=1; k<=i; k++) {
				System.out.print("*");
			}
			System.out.println("");
		}		
	}

}
```



## 10871 : X보다 작은 수

정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		
		StringTokenizer str = new StringTokenizer(br.readLine());
		
		int a = Integer.parseInt(str.nextToken());
		int b = Integer.parseInt(str.nextToken());
		
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i<a; i++){
			int c = Integer.parseInt(st.nextToken());
			
			if(c<b) {
				bw.write(c+" ");
			}

		}
		bw.flush();
		bw.close();
		
	}

}
```

