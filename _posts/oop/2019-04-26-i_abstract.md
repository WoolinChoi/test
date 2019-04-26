---
layout: post
title: abstract
category: oop
tags: [java, oop, abstract]
comments: false
---

# [abstract]()

## 오늘의 학습
~~~java
1. abstract - 미완성, overriding의 강제성 주려고, overriding은 다형성주려고

2. final - 변경불가

3. interface - 구조(틀)

// interface는 100% 추상, 표준화시키기위해서
interface B{
    inte B;    // public static final
    void B(); // public abstract
}
class BB implements B{
    void B(){}
}
// abstract는 하나가 추상이면 클래스도 추상시켜줘야한다
class A {
    int A;
    A{}{}
    void A(){}
    abstract void AA();
}
class B extends A{
    void AA(){}
}
~~~

## Item
~~~java
// 부모클래스
public abstract class Item {
	protected String no;
	protected String title;
	Item(){
		System.out.println("Item 기본생성자");
	}
	public Item(String no, String title){
		this.no = no;
		this.title = title;
		System.out.println("Item 인자생성자");
	}
	// 미완성은 abstract 추상화한다.
	public abstract void output(); // {} : 함수표시는 아무일도 하지 않지만 완벽한 함수 구현
}
~~~