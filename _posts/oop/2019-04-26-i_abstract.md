---
layout: post
title: abstract
category: oop
tags: [java, oop, abstract]
comments: false
---

# [abstract]()

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