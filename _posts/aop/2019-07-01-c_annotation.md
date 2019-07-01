---
layout: post
title: annotation
category: aop
tags: [java, aop, annotation]
comments: false
---

# [annotation]()

## MainApp
~~~java
package aop3_annotation;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class MainApp {
	public static void main(String[] args) {
		// 스프링 설정 파일 연동
		ApplicationContext ctx = 
				new ClassPathXmlApplicationContext("aop3_annotation/applicationContext.xml");
		
		// targetBean 객체를 얻어와서 함수 호출
		MessageBean bean = ctx.getBean("messageBean", MessageBean.class);
		bean.sayHello(); // 두번째
		System.out.println("--------------------------------");
		bean.engSayHello(); // 두번째
	}
}
~~~

## MessageBean
~~~java
package aop3_annotation;
public interface MessageBean {
	void sayHello();
	void engSayHello();
	void test();
}
~~~

## MessageBeanImpl
~~~java
package aop3_annotation;
import org.springframework.stereotype.Component;
@Component("messageBean")
public class MessageBeanImpl implements MessageBean {
	public void sayHello() {
		System.out.println("sayHello() 호출");
	}

	public void engSayHello() {
		System.out.println("engSayHello() 호출");
	}

	public void test() {
		System.out.println("text() 호출");
	}
}
~~~

## LoggingAdvice
~~~java
package aop3_annotation;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;
@Aspect
@Component
public class LoggingAdvice {
	@Around("execution(public * aop3_annotation.*.*Hello(..))")
	public Object around(ProceedingJoinPoint point) throws Throwable {
		String methodName = point.getSignature().getName();
		System.out.println("[사전작업] : " + methodName);				// 첫번째
		Object obj = point.proceed();
		System.out.println("<사후작업> : " + methodName);				// 세번째
		return obj;
	}
}
~~~

## ApplicationContext_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:aop="http://www.springframework.org/schema/aop"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd
		http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-4.3.xsd">
<!-- 빈 객체 생성 -->
<context:component-scan base-package="aop3_annotation"></context:component-scan>

<!-- aop 설정 -->
<aop:aspectj-autoproxy/>
</beans>
~~~