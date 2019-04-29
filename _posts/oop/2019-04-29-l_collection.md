---
layout: post
title: collection
category: oop
tags: [java, oop, collection]
comments: false
---

# [collection]()

## ArrayListEx
~~~java
/*
 * 1. list 구조
 *     - 순서를 저장
 */
import java.util.ArrayList;
import java.util.Collections;
public class ArrayListEx {
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<String>(4); // 동적인 배열
		// list 추가하기
		list.add("rabbit");
		list.add("dog");
		list.add("cat");
		list.add("zebra");
		list.add("fox");
		list.add("lion");
		for(String str : list) {
			System.out.println(str);
		}
		System.out.println(list.toString());
		// list 변경하기
		list.set(2, "ant");
		System.out.println(list);
		// list 제거하기
		list.remove(4);
		System.out.println(list);
		// list 정렬하기
		Collections.sort(list);
		System.out.println(list);
//		for(int i = 0; i < list.size(); i++) {
//			String str = (String)list.get(i);
//			System.out.println(str);
//		}
	}
}
~~~

## ArrayListEx2
~~~java
import java.util.*;
public class ArrayListEx2 {
	public static void main(String[] args) {
		ArrayList<Student> data = method();
		// 여기서 출력
		// 향상 된 for문
//		for(Student str : data) { // 자료형을 맞춰준다
//			System.out.println(str);
//		}
		// 표준화 출력
		// Enumeration -> Iterator
		Iterator it = data.iterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
	}
	static ArrayList<Student> method() {
		ArrayList<Student> list = new ArrayList<Student>();
		Student a = new Student("홍길자", 20);
		Student b = new Student("홍길숙", 30);
		Student c = new Student("홍길동", 40);
		list.add(a);
		list.add(b);
		list.add(c);
		return list;
	}
}
class Student {
	String name;
	int age;
	Student(String name, int age) {
		this.name = name;
		this.age = age;
	}
	public String toString() {
		return name + "님은" + age + "세입니다";
	}
}
~~~

## HashSetEx
~~~java
import java.util.HashSet;
public class HashSetEx {
	public static void main(String[] args) {
		HashSet<String> list = new HashSet<String>(); // 순서를 저장하지 않는다
		list.add("rabbit");
		list.add("dog");
		list.add("rabbit"); // 중복된 값은 들어가지 않는다
		list.add("zebra");
		list.add("zebra");
		list.add("lion");
		System.out.println(list);
	}
}
~~~

## HashSetLotto
~~~java
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
public class HashSetLotto {
	public static void main(String[] args) {
		HashSet<Integer> lotto = new HashSet<Integer>();
		while(lotto.size() < 6) {
			int su = (int)(Math.random() * 45) + 1;
			lotto.add(su);
		}
		System.out.println(lotto);
		ArrayList<Integer> list = new ArrayList<Integer>(lotto);
		Collections.sort(list);
	}
}
~~~

## TreeSetEx 
~~~java
import java.util.TreeSet;
public class TreeSetEx {
	public static void main(String[] args) {
		TreeSet set = new TreeSet();
		set.add("lion");
		set.add("ant");
		set.add("snake");
		set.add("dog");
		set.add("cat");
		set.add("elephant");
		set.add("zebra");
		set.add("bee");
		set.add("tiger");
		System.out.println(set);
		System.out.println(set.subSet("d", "s"));
		System.out.println(set.headSet("d"));
		System.out.println(set.tailSet("d"));
	}
}
~~~

## HashMapEx
~~~java
import java.util.HashMap;
import java.util.Scanner;
public class HashMapEx {
	public static void main(String[] args) {
		HashMap<String, String> map = new HashMap<String, String>();
		map.put("kimjava", "1111");
		map.put("parkjava", "1234");
		map.put("leejava", "1234");
		map.put("kimjava", "9999");
		Scanner input = new Scanner(System.in);
		boolean stop = false;
		while(!stop) {
			System.out.println("아이디와 패스워드 입력");
			System.out.println("아이디 입력->");
			String id = input.nextLine();
			System.out.println("패스워드 입력->");
			String pw = input.nextLine();
			// 아이디가 map에 key에 해당되는가?
			if(map.containsKey(id)) {
				// 그 아이디와 같은 key의 값과 입력받은 패스워드가 같다면
				if(map.get(id).equals(pw)) {
					System.out.println("로그인성공");
					stop = true;
				}else {
					System.out.println("비밀번호가 일치하지 않습니다");
					continue;
				}
			}else {
				System.out.println("존재하지 않는 아이디입니다");
				continue;
			}
		}
	}
}
~~~