---
layout: post
title: recursive
category: javabasic
tags: [java, recursive, ASumTest, Factorial, Fibonacci]
comments: false
---

# [recursive]()

## AsumTest
~~~java
public class ASumTest {
//	public static void main(String[] args) {
//		int sum = 0;
//		for(int i=1; i<=10; i++) {
			// sum+=i;		
//			int exsum = sum;
//			sum = exsum + i;
//			System.out.println(sum+"="+exsum+"+"+i);
//		}
//		System.out.println("합: "+sum); // 55
//	}
//}
	public static void main(String[] args) {
		int sum=0;
		sum = sumFunc(3);
		System.out.println("총합: "+sum);
	}	
	static int sumFunc(int i) {
		if(i==1) return 1;
		return i + sumFunc(i-1);
	}
}
~~~

## Factorial
~~~java
public class Factorial {
	// 5! = 5*4*3*2*1 = 120
	public static void main(String[] args) {
		int n = 5;
		int result = Factorial(n);
		System.out.println("결과: "+result);
	}
	static int Factorial(int n) {
		if(n==1) return 1;
		return n * Factorial(n-1);
	}
}
~~~

## Fibonacci
~~~java
public class Fibonacci {
	// 1 1 2 3 5 8 
	public static void main(String[] args) {
		int n = 5;
		int result = fib(n);
		System.out.println("결과: "+result);
	}
	static int fib(int n) {
		if(n == 1) return 1;
		if(n == 2) return 2; 
		return fib(n-1) + fib(n-2);
	}
}
~~~

## 문제
[문제1] f(4)를 호출한다면?
~~~java
public static void f ( int N ) {
    System.out.println(N);
    if( N > 0 ) f ( N-1);
}
~~~
[풀이]
~~~shell
4 f(3)
4 3 f(2)
4 3 2 f(1)
4 3 2 1
~~~
[답]
~~~shell
4 3 2 1
~~~

## 문제
[문제2] g(4)를 호출한다면?
~~~java
public static void g ( int N) {
    if( N > 0 ) g( N-1);
    System.out.println(N);
}
~~~
[풀이]
~~~shell
g(3) 4
g(2) 3 4
g(1) 2 3 4
g(0) 1 2 3 4
0 1 2 3 4
~~~
[답]
~~~shell
0 1 2 3 4
~~~

 ## 문제
 [문제3] h(4)를 호출한다면?
 ~~~java
public static void h ( int N ) {
    System.out.println(N);
    if( N > 0 ) h ( N -2 );
    System.out.println(N);
}
~~~
[풀이]
~~~shell
4 h(2) (4)
4 2 h(0) (2) (4)
4 2 0 0 2 4
~~~
[답]
~~~shell
4 2 0 0 2 4
~~~