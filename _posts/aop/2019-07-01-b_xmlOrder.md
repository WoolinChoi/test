---
layout: post
title: xmlOrder
category: aop
tags: [java, aop, xmlOrder]
comments: false
---

# [xmlOrder]()

## MainApp
~~~java
package aop2_xml_order;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class MainApp {
	public static void main(String[] args) {
		ApplicationContext ctx = 
				new ClassPathXmlApplicationContext("aop2_xml_order/applicationContext.xml");
		
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
package aop2_xml_order;
public interface MemberBean {
	void register();
	boolean update(String name);
}
~~~

## MemberBeanImpl
~~~java
package aop2_xml_order;
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
package aop2_xml_order;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
public class LoggingAdvice {
	// around는 proceeding기능이 필요하다.
	public Object around(ProceedingJoinPoint point) throws Throwable {
		String methodName = point.getSignature().getName();
		System.out.println("[사전작업] : " + methodName);				// 두번째
		Object obj = point.proceed();
		System.out.println("<사후작업> : " + methodName);				// 다섯번째
		return obj;
	}
	
	public void before(JoinPoint point) throws Throwable {
		String methodName = point.getSignature().getName();
		System.out.println("[*****사전작업*****] : " + methodName);	// 세번째
	}
}
~~~

## LoggingAdvice2
~~~java
package aop2_xml_order;
import org.aspectj.lang.JoinPoint;
public class LoggingAdvice2 {
	public void before(JoinPoint p) {
		System.out.println("before------>" + p); // 첫번째
	}
	
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
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-4.3.xsd">
<!-- member 빈 객체 생성 -->
<bean id="memberBean" class="aop2_xml_order.MemberBeanImpl"/>

<!-- advice 빈 객체 생성 : 부가기능 -->
<bean id="advice" class="aop2_xml_order.LoggingAdvice"/>
<bean id="advice2" class="aop2_xml_order.LoggingAdvice2"/>

<!-- aop 설정 -->
<aop:config>
	<!-- Advice를 적용할 타켓의 메소드를 선별하는 정규표현식 -->
	<aop:pointcut expression="execution(public * *(..))" id="pointCut"/>
	
	<!-- aspect는 부가기능 : 빈 id가 들어가야한다 -->
	<aop:aspect id="aspect" ref="advice" order="2">
		<!-- Advice:around 공통기능 -->
		<aop:around method="around" pointcut-ref="pointCut"/>
		<aop:before method="before" pointcut-ref="pointCut"/>
	</aop:aspect>
	
	<aop:aspect id="aspect2" ref="advice2" order="1">
		<aop:before method="before" pointcut-ref="pointCut"/>
		<aop:after-returning method="afterReturning" pointcut-ref="pointCut"/>
	</aop:aspect>
</aop:config>
</beans>
~~~