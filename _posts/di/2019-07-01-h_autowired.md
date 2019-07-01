---
layout: post
title: autowired
category: di
tags: [java, di, autowired]
comments: false
---

# [autowired]()

## MainApp
~~~java
package ex3_autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class MainApp {
	public static void main(String[] args) {
		ApplicationContext ctx = 
				new ClassPathXmlApplicationContext(
						"ex3_autowired/applicationContext.xml");
		
		MessageBean bean = ctx.getBean("message", MessageBean.class);
		bean.sayHello();
	}
}
~~~

## MessageBean
~~~java
package ex3_autowired;
public interface MessageBean {
	void sayHello();
}
~~~

## MessageBeanImpl
~~~java
package ex3_autowired;
import java.io.IOException;
import javax.annotation.Resource;
public class MessageBeanImpl implements MessageBean {
	private String name;
	private String message;
	
//	@Autowired // 값지정 - 생성자 or setter or @annotation
//	@Qualifier("outputer2")
	@Resource(name="outputer")
	private Outputer out;
	
	// 값 지정 - 생성자 or setter
	public void setName(String name) {
		this.name = name;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	
	public void sayHello() {
		System.out.println(name + "님 " + message);
		
		try {
			out.writeMessage(name + "님 " + message);
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}
~~~

## Outputer
~~~java
package ex3_autowired;
import java.io.IOException;
public interface Outputer {
	void writeMessage(String msg) throws IOException;
}
~~~

## OutputerImpl
~~~java
package ex3_autowired;
import java.io.FileWriter;
import java.io.IOException;
public class OutputerImpl implements Outputer {
	private String path;
	
	// 값지정 - 생성자 or setter
	public void setPath(String path) {
		this.path = path;
	}
	
	public void writeMessage(String msg) throws IOException {
		FileWriter f = new FileWriter(path);
		f.write(msg);
		f.close();
	}
}
~~~

## ApplicationContext_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">
<!-- 빈객체 생성 -->
<bean id="message" class="ex3_autowired.MessageBeanImpl">
	<!-- setName()호출 -->
	<property name="name" value="지각자"/>
	
	<!-- setMessage() 호출 --> 
	<property name="message">
		<value>조원들께쏘세요</value>
	</property>
</bean>

<!-- @anntation 찾기 -->
<context:component-scan base-package="ex3_autowired"></context:component-scan>
<bean id="outputer" class="ex3_autowired.OutputerImpl">
	<property name="path" value="src\\ex3_autowired\\save.txt"/>
</bean>
<bean id="outputer2" class="ex3_autowired.OutputerImpl">
	<property name="path" value="src\\ex3_autowired\\message.txt"/>
</bean>
</beans>
~~~