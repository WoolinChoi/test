---
layout: post
title: operator
category: javabasic
tags: [java, operator]
comments: false
---

# [operator]()

## 오늘의 목표
~~~shell
1. 연산자

JVM : 자바를 구동하는 가상머신
자바는 서버와 운영체제로부터 종속적이지 않습니다.
~~~

## IncDec
~~~java
/*
 * 증가 감소 연산자 : ++, --
 */
public class Ex01_IncDec {
	public static void main(String[] args) {
		int a=5, b=7;
//		System.out.println("A=" + (a + 1) + ", B=" + (b + 1) ); // ()를 넣어준다. a = 6, b = 8
//		a = a + 1;
//		b = b - 1;
//		System.out.println("A=" + a + ", B=" + b); // a = 6, b = 6
//		a++;
//		b--;
//		System.out.println("A=" + a + ", B=" + b); // a = 7, b = 5		
//		++a;
//		--b;
//		System.out.println("A=" + a + ", B=" + b); // a = 7, b = 5
//		int result = ++a;
//		System.out.println("Result=" + result + ", A=" + a); // result = 6, A = 6
//		int result2 = a++;
//		System.out.println("Result=" + result2 + ", A=" + a); // result = 6, A = 7
		System.out.println("A=" + ++a + ", B=" + --b); // A = 6, B = 6
		System.out.println("A=" + a++ + ", B=" + b--); // A = 6, B = 6
		System.out.println("A=" + a + ", B=" + b);   // A = 7, B = 5	
	}
}
~~~

## Not
~~~java
/*
 * not : 결과를 반대로 하는 연산자
 * 		- 일반논리(true/false) : !
 * 		- 이진논리(비트의 값: 0/1) : ~
 */
public class Ex02_Not {
	public static void main(String[] args) {
			boolean result = 3 > 4;
			System.out.println(result); // false
			System.out.println(!result); // true
			int a = 15;
			System.out.println(~a); // 음수, +(0)에서 이진논리로 인해서 -(1)이 된다.
	}
}

~~~