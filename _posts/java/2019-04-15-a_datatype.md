---
layout: post
title: datatype
category: javabasic
tags: [java, datatype]
comments: false
---

# [datatype]()

## 오늘의 목표
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

## [문제1]
자바의 변수명을 지정하는 규칙으로 잘못된 것은?
~~~shell
(1)한글을 사용할 수 없다.
(2)‘$’와 ‘_’를 문자와 숫자의 조합에 사용할 수 있다.
(3)길이 제한이 없다.
(4)대소문자를 구별한다.
(5)첫번째 글자는 숫자와 ‘$’, ‘_’는 올 수 없다.
/*
 * 1, 5
 */
~~~

## [문제2]
자바의 변수명으로 적합한 것은?
~~~shell
(1) abstract                  (2)  3Color                    (3) color3
(4) 변수                      (5)  abcdefghijklmnopqrstuvwxyz
(6) color-number              (7)  the color
/*
 * 3, 4, 5
 */
~~~

## [문제3]
자바의 변수명을 지정하는 규칙에 맞는 것은?
~~~shell
(1)%this                         (2)3this                        (3) This
(4) this-3                       (5) this                        (6) $this
/*
 * 3, 6
 */
~~~

## [문제4]
자바의 예약어가 아닌 것을 것은?
~~~shell
(1)if                           (2) main                        (3) boolean
(4)null                         (5) true                        (6)do
/*
 * 2
 */
~~~

## [문제5]
다음 중 변수명으로 사용할 수 없는 것은?
~~~shell
(1)$ystem                   (2) new                         (3) m@n
(4)system_host              (5) 1cup                        (6) NULL
/*
 * 2, 3, 5
 */
~~~

## [문제6]
정수형 byte 타입의범위는?
~~~shell
(1)27 ~ 27-1                  (2)0 ~ 28                      (3)-28 ~ 28-1
(4)-27 ~ 27-1                 (5)-27-1 ~ 27                 
/*
 * 4
 */
~~~

## [문제7]
다음 중에서 잘못된 것은?
~~~shell
(1)int i = 12345678;                           (2)float f = 3.5;
(3)double d = 12345678.0;                      (4)String s = “”;
/*
 * 2
 */
~~~

## [문제8]
다음 프로그램의 결과는?
~~~java
class Test {
    public static void main ( String  [] args ) {
    byte a = 64;
    byte b = 64;
    byte result = a + b;
    System.out.println("result = " + result );
    }
}
/*
 * 4
 */
~~~
~~~shell
(1)127              (2) 128              (3) -128             (4) 컴파일 에러
~~~

## [문제9]
다음프로그램의 결과는?
~~~java
class Test {
    public static void main ( String  [] args ) {
        byte b = 36;
        int i = ( int ) b;
        System.out.println( "b = " + b );
        System.out.println( "i = " + i );
    }
}
/*
 * b = 36
 * i = 36
 */
~~~

## [문제10]
다음프로그램의 결과는?
~~~java
class Test {
    public static void main ( String  [] args ) {
        int  i = 360;
        byte  b = ( byte ) i;
        System.out.println( "i = " + i );
        System.out.println( "b = " + b ); 
    }
}
/*
 * i = 360
 * b = 104
 */
~~~

## [문제11]
다음 중 형변환을 생략이 가능한 것은?
~~~java
byte  b = 127;
char  ch = ‘글’;
int   i = 20000000;
long  l =  1L;
/*
 * 2, 3, 4
 */
~~~
~~~shell
(1)b = ( byte ) i;
(2)i = ( int ) ch;
(3)int  var = ( int ) b;
(4)float  f = (float) l;
(5) l = (long)i;
~~~