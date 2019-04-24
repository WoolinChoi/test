---
layout: post
title: operator
category: javabasic
tags: [java, operator]
comments: false
---

# [operator]()

## 오늘의 학습
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

## Arithmetic
~~~java
/*
 * 산술연산자 : *  /  %, +  -
 */
public class Ex03_Arithmetic {
	public static void main(String[] args) {
		// 1. 숫자하나를 입력받기(Scanner - import java.util.*)
		// 2. 홀수인지 짝수인지 연산하여 출력(% : 나머지 연산자)
		Scanner input = new Scanner(System.in);
		System.out.println("숫자 하나 입력=>");
		int su = input.nextInt();
		if( su % 2 == 0) {
			System.out.println("짝수");
		}else {
			System.out.println("홀수");
		}
	}
}
~~~

## Comparable
~~~java
/*
 * 비교연산자 : >  <  >=  <=, ==  !=
 */
public class Ex04_Comparable {
	public static void main(String[] args) {
		int k = 100, e = 100, m = 100;
		double avg = (double)(k + e + m) / 3;
		System.out.println("평균: " + avg);
		String score = "";
//		if(avg >= 90) {
//			System.out.println("A학점");
//		}else if(avg >= 80) {
//			System.out.println("B학점");
//		}else if(avg >= 70) {
//			System.out.println("C학점");
//		}
		switch((int)(avg / 10)) {
		case 10:
		case 9: score = "A학점"; break;
		case 8: score = "B학점"; break;
		case 7: score = "C학점"; break;
		case 6: score = "D학점"; break;
		default: score = "F학점";
		}
		System.out.println("학점: " + score);
	}
}
~~~

## GenneralLogical
~~~java
/* 논리연산자
 * 	- 일반 논리(true/false) : &&  ||
 * 	- 이진 논리(bit에 있는 1/0) : &  |  ^
 */
public class Ex05_GenneralLogical {
	public static void main(String[] args) {	
		// 문자 하나를 입력받아
		// (1) 대문자인지 출력
		// (2) 대문자인지 소문자인지 그외인지 출력
		Scanner input = new Scanner(System.in);
		System.out.print("문자 하나 입력=>");
		char ch = input.next().charAt(0); // 기본형만 casting 된다.
//		if(Character.isUpperCase(ch) == true) {
//			System.out.println("대문자입니다.");
//		}else if(Character.isLowerCase(ch) == true){
//			System.out.println("소문자입니다.");
//		}else {
//			System.out.println("잘못입력했습니다.");
//		}
		// 문자 'A'보다 크거나 같고, 'Z'보다 작거나 같으면 => 대문자
		// 그렇지않으면 대문자 아님
		if(ch >= 'A' && ch <= 'Z') {
			System.out.println("대문자");
		}else if(ch >= 'a' && ch <= 'z'){
			System.out.println("소문자");
		}else {
			System.out.println("그 외");
		}
		/*
		int 성적 = 75;
		char 태도 = 'A';
		// 성적향상반 조건 - 80점이상이고 태도는 'A'이어야 함
		if(성적 >= 80 && 태도 == 'A') {
			System.out.println("성적향상반");
		}
		// 우등생 조건 - 성적은 80점이상이거나 태도는 'A'이면 가능
		if(성적 >= 80 || 태도 == 'A') {
			System.out.println("성적향상반");
		}
		*/
	}
}
~~~

## BinaryLogical
~~~java
public class Ex06_BinaryLogical {
	public static void main(String[] args) {
		int a = 15, b = 10;
		int and = a & b;
		int or = a | b;
		int xor = a ^ b;
		System.out.println(and); // 1010, 10
		System.out.println(or); // 1111, 15
		System.out.println(xor); // 0101, 5
	}
}
~~~

## Shift
~~~java
/*
 * Shift : 모든 비트의 값을 이동하는 연산자
 * 
 * >> : 오른쪽이동
 * << : 왼쪽이동
 * >>> : 오른쪽이동(부호에 0)
 */
public class Ex07_Shift {
	public static void main(String[] args) {
		int a = 4; // +(0), -(1)값은 유지된다.
		System.out.println(a >> 2); // 0001, 1
		System.out.println(a << 1); // 1000, 8
	}
}

~~~

## ShortCircuitLogic
~~~java
/*
 * 숏서킷로직 : 일반논리에 적용
 */
public class Ex08_ShortCircuitLogic {
	public static void main(String[] args) {
		int a = 3;
		if(a > 3 && ++a > 3) {
			System.out.println("조건만족"); // 출력여부, false
		}
		System.out.println("A=" + a); // a=?, 3 
		if(a > 1 || ++a > 3) {
			System.out.println("조건만족2"); // true
		}
		System.out.println("A=" + a); // a=?, 3
		/*
	    int a = -5;
	    if ( ( a > 0 ) & ( ( ++a / 3 ) > 0 ) ) {
	           a++;
	    }
	    System.out.println( a );  // 일반논리였으면 -5, 이진논리를넣으면 -4
		*/
		// 우리가 생각하는대로 바꾸려면 일반논리자리에 이진논리를 넣는다.
		// if(a > 1 || ++a > 3) => if(a > 1 | ++a > 3)
		int z = 10 - 7 ^ 3 + 1 * 2 & 4; // 0111 7
		System.out.println(z);
	}
}
~~~

## Samhang
~~~java
/*
 * 삼항연산자
 * 		(조건)? A : B
 * 		조건이 true이면 A 실행하고 false이면 B 실행한다.
 */
public class Ex09_Samhang {
	public static void main(String[] args) {
//		int score = 70;
//		String result = (score >= 80)? "합격" : "불합격";
//		System.out.println(result);
		// [문제] 두수를 입력받아 큰 수를 출력(삼항연산자 이용)
//		Scanner input = new Scanner(System.in);
//		System.out.print("첫번째 숫자=>");
//		int su = input.nextInt();
//		System.out.print("두번째 숫자=>");
//		int su2 = input.nextInt();
//		int max = (su > su2)? su : su2;
//		System.out.println("큰수: " + max);	
//		[삼항연산자] 세 정수가 A, B, C가 주어진다. 이 때, 두번째로 큰 정수를 출력하는 프로그램을 작성하시오.
		Scanner input = new Scanner(System.in);
		System.out.println("세 정수를 입력하시오.");
		int a = input.nextInt();
		int b = input.nextInt();
		int c = input.nextInt();
		int second = ((a >= b && b >= c && a >= c) || (c >= b && b >= a && c >= a))? 
				b : ((b >= a && a >= c && b >= c) || (c >= b && b >= a && c >= a))? a : c;
		System.out.println("두번째 큰수:" + second);
	}
}
~~~

## Assignment 
~~~java
/*
 * 대입연산잔 : = 
 * 		- 축약대입연산자(산술/이진논리/쉬프트)
 */
public class Ex10_Assignment {
	public static void main(String[] args) {
		int a = 10, b = 7;
		a += b; // a = a + b;
		System.out.println("A= " + a); // 17
		a -= b;
		System.out.println("A= " + a); // 10
		a *= b;
		System.out.println("A= " + a); // 70
		a %= b;
		System.out.println("A= " + a); // 0
		a /= b;
		System.out.println("A= " + a); // 0
	}
}
~~~