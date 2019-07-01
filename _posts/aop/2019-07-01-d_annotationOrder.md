---
layout: post
title: annotationOrder
category: aop
tags: [java, aop, annotationOrder]
comments: false
---

# [annotationOrder]()

## MainApp
~~~java
package aop4_annotation_order;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class MainApp {
	public static void main(String[] args) {
		ApplicationContext ctx = 
				new ClassPathXmlApplicationContext("aop4_annotation_order/applicationContext.xml");
		
		// memberBean 객체를 얻어와서 함수 호출
		MemberBean bean = ctx.getBean("memberBean", MemberBean.class);
		bean.register(); // 네번째
		
		System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
		
		bean.update("홍길동"); // 네번째
	}
}
~~~

## MemberBean
~~~java
package aop4_annotation_order;
public interface MemberBean {
	void register();
	boolean update(String name);
}
~~~

## MemberBeanImpl
~~~java
package aop4_annotation_order;
import org.springframework.stereotype.Component;
@Component("memberBean")
public class MemberBeanImpl implements MemberBean {
	public void register() {
		System.out.println("register 함수 호출");
	}

	public boolean update(String name) {
		System.out.println(name + "님 update 호출");
		return false;
	}
}
~~~

## LoggingAdvice
~~~java
package aop4_annotation_order;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;
@Order(2)
@Aspect
@Component
public class LoggingAdvice {
	// around는 proceeding기능이 필요하다.
	@Around("execution(public * *(..))")
	public Object around(ProceedingJoinPoint point) throws Throwable {
		String methodName = point.getSignature().getName();
		System.out.println("[사전작업] : " + methodName);				// 두번째
		Object obj = point.proceed();
		System.out.println("<사후작업> : " + methodName);				// 다섯번째
		return obj;
	}
	@Before("execution(public * *(..))")
	public void before(JoinPoint point) throws Throwable {
		String methodName = point.getSignature().getName();
		System.out.println("[*****사전작업*****] : " + methodName);     // 세번째
	}
}
~~~

## LoggingAdvice2
~~~java
package aop4_annotation_order;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;
@Order(1)
@Aspect
@Component
public class LoggingAdvice2 {
	@Before("execution(public * *(..))")
	public void before(JoinPoint p) {
		System.out.println("before------>" + p); // 첫번째
	}
	@AfterReturning("execution(public * *(..))")
	public void afterReturning(JoinPoint p) {
		System.out.println("afterReturn------->" + p); // 여섯번째
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
<context:component-scan base-package="aop4_annotation_order"></context:component-scan>

<!-- aop 설정 -->
<aop:aspectj-autoproxy/>
</beans>
~~~