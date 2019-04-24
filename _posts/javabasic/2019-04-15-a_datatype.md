---
layout: post
title: datatype
category: javabasic
tags: [java, datatype]
comments: false
---

# [datatype]()

## 오늘의 학습
~~~shell
1. JDK 설치
	- JAVA.HOME
	- Path에 추가   %JAVA_HOME%\bin

2. IDE -> eclipse

3. 변수 : 값 하나를 메모리에 저장하기 위해 메모리 이름
    + 
   데이타 타입
	(1) 기본형
		- 논리형 : boolean
		- 문자형 : char
		- 정수형 : int / long
		- 실수형 : double

	(2) 참조형 : 클래스, 배열
		new 연산자 이용해서 heap에 메모리 할당

	[#] string
~~~

## Naming
~~~java
/*
 * 데이타 타입(자료형)
 * 1. 기본형(프리미티브)
 *		논리형 : boolean
 *		문자형 : char
 *		정수형 : int / long
 *		실수형 : double
 *
 * 2. 참조형(레퍼런스) : 클래스, 배열 
 * 		-> new 연산자를 이용해서 메모리 할당(확보)
 * 		ex) String(new를 안써도 되는 예외)
 */

// 한줄주석
/*
      여러줄 주석
 */
/**
      도움말 주석
 */
public class Ex01_Naming {
	public static void main(String[] args) {
		// 1. 변수선언
		char a;
		int b;
		double c;
		// 2. 값 지정
		a = '김';	    // char형은 ''으로 문자 하나만 지정
		b = 1000000000;	// int형은 21억아래로 지정 
		c = 100.3;
	}
}
~~~

## Caution
~~~java
public class Ex02_Caution {
	public static void main(String[] args) {
		// 실수형
		// float f;	// 4Byte
		double f;
		f = 3.6;
		System.out.println("실수:" + f);
		// 문자형-정수형
		char ch;
		ch = 65;
		System.out.println("ch값:" + ch);
		// int i;
		// i = 'a';
		int i = 'a';
		System.out.println("i값:" + i);
		long l = 10000000000L;
		System.out.println("l값:" + l);
		// int i2 = 1000000000;
		// 형변환 - casting
		double db = (double)100;
		System.out.println("db값:" + db);
		int in = (int)100.1;	// 메모리가 적을때 ()에 자료형을 넣어 casting을 해준다.
		System.out.println("in값:" + in);	
	}
}
~~~

## Declaration
~~~java
public class Ex03_Declaration {
	public static void main(String[] args) {
		// (1) 변수 선언 -> 값 대입
		int kor;
		kor = 30;
		// (2) 초기화 = 변수 선언 + 값 지정(대입)
		int eng = 33;
		if(kor == eng) {
			System.out.println("같다");
		}else {
			System.out.println("다르다");
		}
		int temp;	// swap
		temp = kor;
		kor = eng;
		eng = temp;
		System.out.println("국어:" + kor + ", 영어:" + eng);
		System.out.printf("국어:%d, 영어:%d", kor, eng);
		}
}
~~~

## String
~~~java
public class Ex04_String {
	public static void main(String[] args) {
		int i = 10;
		String a = new String("홍길동");
		String b = new String("홍길동");
		// 주소를 비교한다.
		if(a == b) {
			System.out.println("같다");
		}else {
			System.out.println("다르다");
		}
		// 값을 비교한다. String은 equals를 써야한다.
		if(a.equals(b)) {
			System.out.println("이름이 같다");
		}else {
			System.out.println("이름이 다르다");
		}
	}
}
~~~

## Scanner
~~~java
import java.util.Scanner;
// import java.lang.*;	// *로 모두 import 해준다.
// ctrl + shift + o
public class Ex05_Scanner {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		// 학생명을 입력 받아
		System.out.println("학생이름입력=>");
		String name = input.nextLine();	
		System.out.print("국어점수=>");
		int kor = input.nextInt();
		System.out.print("영어점수=>");
		int eng = input.nextInt();
		System.out.print("수학점수=>");
		int math = input.nextInt();
		// 총점을 구해서 출력
		int total = kor + eng + math;
		System.out.println("총점: " + total);
		// 평균을 구해서 출력
		double avg = (double)total/3;	// int형과 int형을 계산하면 int형으로 계산되니 double형으로 casting해준다.
		System.out.println("평균: " + avg);
	}
}
~~~