---
layout: post
title: xmlPvalue
category: di
tags: [java, di, xmlPvalue]
comments: false
---

# [xmlPvalue]()

## MainApp
~~~java
package ex1_xml3_pvalue;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class MainApp {
	public static void main(String[] args) {
		ApplicationContext context =
				new ClassPathXmlApplicationContext("ex1_xml3_pvalue/applicationContext.xml");
		
		MemberDAO dao = context.getBean("dao1", MemberDAO.class);
		dao.insert();
	}
}
~~~

## MemberBean
~~~java
package ex1_xml3_pvalue;
public class MemberBean {
	private String name;
	private int age;
	private String message;
	
	public MemberBean() {}
	
	public MemberBean(String name, int age, String message) {
		super();
		this.name = name;
		this.age = age;
		this.message = message;
	}
	
	// getter, setter
	public String getName() {
		return name;
	}
	public int getAge() {
		return age;
	}
	public String getMessage() {
		return message;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	
	// 변수가 private로 잡혀 있기 때문에, 멤버변수를 출력할 수 있는 public을 만들어준다.
	public void output() {
		System.out.println(name + "(" + age + ") " + message);
	}
}
~~~

## MemberDAO
~~~java
package ex1_xml3_pvalue;
public class MemberDAO {
	private MemberBean member;
	
	public MemberDAO() {}
	
	public MemberDAO(MemberBean member) {
		this.member = member;
	}
	
	public void setMember(MemberBean member) {
		this.member = member;
	}
	
	public void insert() {
		System.out.println(member.getName() + "님 정보가 입력");
	}
}
~~~

## ApplicationContext_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
<!-- p의 참조형은 ref를 붙혀준다. -->
<bean id="mem1" class="ex1_xml3_pvalue.MemberBean" p:name="홍길동" p:age="33" p:message="오늘의 점심은"/>
<bean id="dao1" class="ex1_xml3_pvalue.MemberDAO" p:member-ref="mem1"/>
</beans>
~~~