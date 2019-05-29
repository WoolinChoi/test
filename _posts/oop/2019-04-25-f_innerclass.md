---
layout: post
title: innerclass
category: oop
tags: [java, oop, innerclass]
comments: false
---

# [innerclass]()

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