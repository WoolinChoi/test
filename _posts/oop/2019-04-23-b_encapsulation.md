---
layout: post
title: encapsulation
category: oop
tags: [java, oop, encapsulation]
comments: false
---

# [encapsulation]()

## Main
~~~java
public class Main {
	public static void main(String[] args) {
		Student s = new Student();
		s.setName("홍길동");
		s.setKor(100);
		s.setEng(88);
		s.setMath(77);
		System.out.println("이름: " + s.getName());
		System.out.println("총합: " + s.calTotal());
		System.out.println("평균: " + s.calAverage());
	}
}
~~~

## Student
~~~java
/*
 *  캡슐화: 권한관련부여
 *  1. 멤버변수 - private(다른클래스에서 접근 허용 안함)
 *  2. 멤버메소드 - public(모든 접근 허용)
 */
public class Student {
	private String name;				// 멤버변수
	private int kor, eng, math;
	private int total;
	private double avg;
	public int calTotal() {				// 멤버메소드
		total = kor + eng + math;
		return total;
	}
	public double calAverage() {
		avg = (double) total / 3;
		return avg;
	}
	// setter/getter
	public void setName(String name) {
		this.name = name;
	}
	public void setKor(int kor) {
		this.kor = kor;
	}
	public void setEng(int eng) {
		this.eng = eng;
	}
	public void setMath(int math) {
		this.math = math;
	}
	public String getName() {
		return name;
	}
	public int getKor() {
		return kor;
	}
	public int getEng() {
		return eng;
	}
	public int getMath() {
		return math;
	}	
}
~~~

## [복습]
![문제1](/assets/post-img/java/00.png)
~~~java
public class CalculatorExpr {
	private int num1;
	private int num2;
	private int addition;
	private int substraction;
	private int multiplication;
	private double division;
	public int calAddition() {				
		addition = num1 + num2;
		return addition;
	}
	public int calSubtraction() {				
		substraction = num1 - num2;
		return substraction;
	}
	public int calMultiplication() {				
		multiplication = num1 * num2;
		return multiplication;
	}
	public double calDivision() {				
		division = (double)num1 / num2;
		return division;
	}
	// setter/getter
	public int getNum1() {
		return num1;
	}
	public void setNum1(int num1) {
		this.num1 = num1;
	}
	public int getNum2() {
		return num2;
	}
	public void setNum2(int num2) {
		this.num2 = num2;
	}
	public int getAddition() {
		return addition;
	}
	public void setAddition(int addition) {
		this.addition = addition;
	}
	public int getSubstraction() {
		return substraction;
	}
	public void setSubstraction(int substraction) {
		this.substraction = substraction;
	}
	public int getMultiplication() {
		return multiplication;
	}
	public void setMultiplication(int multiplication) {
		this.multiplication = multiplication;
	}
	public double getDivision() {
		return division;
	}
	public void setDivision(double division) {
		this.division = division;
	}
}
~~~
~~~java
import java.util.Scanner;
public class CalculatorTest {
	public static void main(String[] args) {
		int[] arrex = inputEx();
		output(arrex[0], arrex[1], false);
		char ch = 'y';
		while(true) {
			System.out.println("다시하시겠습니까? y|n");
			Scanner input2 = new Scanner(System.in);
			ch = input2.next().charAt(0);
			if(ch == 'n') {
				System.out.println("종료되었습니다.");
				break;
			}else if(ch == 'y') {
				int[] arr = inputEx();
				output(arr[0], arr[1], true);
			}else {
				System.out.println("잘못입력하였습니다.");
			}
		}
	}
	static int[] inputEx() {
		Scanner input = new Scanner(System.in);
		System.out.println("첫번째 숫자를 입력해주세요.");
		int num1 = input.nextInt();
		System.out.println("두번째 숫자를 입력해주세요.");
		int num2 = input.nextInt();
		int[] arr = {num1, num2};
		return arr;
	}
	static void output(int num1, int num2, boolean test) {
		CalculatorExpr c = new CalculatorExpr();
		c.setNum1(num1);
		c.setNum2(num2);
		if(test == true) {
			System.out.println("추출된 숫자: " + c.getNum1() + ", " + c.getNum2());
		}
		System.out.println("덧셈: " + c.calAddition());
		System.out.println("뺄셈: " + c.calSubtraction());
		System.out.println("곱셈: " + c.calMultiplication());
		System.out.println("나눗셈: " + c.calDivision());		
	}
}
~~~