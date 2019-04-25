---
layout: post
title: innerclass
category: oop
tags: [java, oop, innerclass]
comments: false
---

# [innerclass]()

## 오늘의 학습
~~~shell
1. inner class

2. 접근지정자
    - private/public
    - protected/default(아무표시없는 경우)

3. 상속(*****)

* 개발자 입장
1. 부모클래스 멤버로 있는 경우 - 그냥 호출
2. 부모클래스에 없는 경우 - 추가
3. 부모클래스에 있는데 수정이 필요 - overriding
~~~

## InnerTest
~~~java
class Outer {
	static class Inner {
		static void najabara() {
			System.out.println("호출해주세요");
		}
	}
}
public class InnerTest {
	public static void main(String[] args) {
//		Outer o = new Outer();
//		Outer.Inner in = o.new Inner();
//		Outer.Inner in = new Outer.Inner();
//		in.najabara();
		Outer.Inner.najabara();
	}
}
~~~