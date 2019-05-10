---
layout: post
title: recursive
category: java
tags: [java, recursive, ASumTest, Factorial, Fibonacci]
comments: false
---

# [recursive]()

## AsumTest
~~~java
public class ASumTest {
//	public static void main(String[] args) {
//		int sum = 0;
//		for(int i = 1; i <= 10; i++) {
			// sum += i;		
//			int exsum = sum;
//			sum = exsum + i;
//			System.out.println(sum + "=" + exsum + "+" + i);
//		}
//		System.out.println("합: " + sum); // 55
//	}
//}
	public static void main(String[] args) {
		int sum=0;
		sum = sumFunc(3);
		System.out.println("총합: " + sum);
	}	
	static int sumFunc(int i) {
		if(i == 1) return 1;
		return i + sumFunc(i - 1);
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
		System.out.println("결과: " + result);
	}
	static int Factorial(int n) {
		if(n == 1) return 1;
		return n * Factorial(n - 1);
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
		System.out.println("결과: " + result);
	}
	static int fib(int n) {
		if(n == 1) return 1;
		if(n == 2) return 2; 
		return fib(n - 1) + fib(n - 2);
	}
}
~~~