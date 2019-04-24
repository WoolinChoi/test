---
layout: post
title: constructor
category: oop
tags: [java, oop, constructor]
comments: false
---

# [constructor]()

## Main
~~~java
public class Main {
	public static void main(String[] args) {
		Student s2 = new Student("홍길자", 100, 80, 70);
		System.out.println("이름: " + s2.getName());
		System.out.println("총합: " + s2.calTotal());
		System.out.println("평균: " + s2.calAverage());
		Student s = new Student();
//		s.setName("홍길동");
//		s.setKor(100);
//		s.setEng(88);
//		s.setMath(77);
		System.out.println("이름: " + s.getName());
		System.out.println("총합: " + s.calTotal());
		System.out.println("평균: " + s.calAverage());
	}
}
~~~

## Student
~~~java
public class Student {
	// 멤버변수(member field)
	private String name;	
	private int kor, eng, math;
	private int total;
	private double avg;
	// 생성자 함수가 하나도 없는 경우
	// Java Compiler가 자동으로 생성
	// -> 기본생성자는 만든다.
	public Student() {
		// this : 멤버를 지칭하기 위한 레퍼런스
//		this.name = "익명";
//		this.kor = 50;
//		this.eng = 50;
//		this.math = 50;
		// this() : 다른 생성자 함수 호출
		//			반드시 첫줄에 기술
		this("익명", 50, 50, 50);
		System.out.println("기본 생성자 호출");
	}
	// 생성자 - 멤버변수 초기화
	// - 클래스명과 동일한 이름의 함수
	// - 리턴형 없음(void 안됨)
	// - overloading 이름은 같은데 인자의 자료형과 갯수는 다르게
	public Student(String name, int kor, int eng, int math) {
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
		System.out.println("인자있는 생성자 호출");
	}
	// 멤버메소드(member method)
	public int calTotal() {		
		total = kor+eng+math;
		return total;
	}
	public double calAverage() {
		avg = (double)total/3;
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
	public int getTotal() {
		return total;
	}
	public double getAvg() {
		return avg;
	}
}
~~~