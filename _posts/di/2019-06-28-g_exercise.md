---
layout: post
title: exercise
category: di
tags: [java, di, exercise]
comments: false
---

# [exercise]()

## Main
~~~java
package exercise;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import exercise.order.domain.Customer;
import exercise.order.service.CustomerService;
public class Main {
	public static void main(String[] args) {
		ApplicationContext ctx = new 	ClassPathXmlApplicationContext("exercise/beans.xml"); 
	
		Customer customer = (Customer)ctx.getBean("customer");
	
		CustomerService customerService = (CustomerService)ctx.getBean("customerService");
		customerService.saveCustomer(customer);
		customerService.deleteCustomer(1);		
	}
}
~~~

## Customer
~~~java
package exercise.order.domain;
import org.springframework.stereotype.Component;
@Component
public class Customer {
	private long id;
	private String name;
	private String address;
	private String email;

	// 2. toString
	public String toString() {
		return "id : " + id + ", name : " + name + ", address : " + address + ", email : " + email;
	}
	
	// 1. setter, gettter
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
}
~~~

## CustomerRepository
~~~java
package exercise.order.repository;
import exercise.order.domain.Customer;
public interface CustomerRepository {
	void save(Customer customer);
	void delete(long id);
}
~~~

## CustomerRepositoryImpl
~~~java
package exercise.order.repository;
import org.springframework.stereotype.Component;
import exercise.order.domain.Customer;
@Component
public class CustomerRepositoryImpl implements CustomerRepository {
	public void save(Customer customer) {
		System.out.println(customer + "가 저장되었습니다.");
	}

	public void delete(long id) {
		System.out.println(id + "번 고객이 삭제되었습니다.");
	}
}
~~~

## CustomerService
~~~java
package exercise.order.service;
import exercise.order.domain.Customer;
public interface CustomerService {
	void saveCustomer(Customer customer);
	void deleteCustomer(long id);
}
~~~

## CustomerServiceImpl
~~~java
package exercise.order.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import exercise.order.domain.Customer;
import exercise.order.repository.CustomerRepository;
@Component("customerService")
public class CustomerServiceImpl implements CustomerService {
	@Autowired
	private CustomerRepository repository;

	public void saveCustomer(Customer customer) {
		repository.save(customer);
	}

	public void deleteCustomer(long id) {
		repository.delete(id);
	}
}
~~~

## Beans_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

<bean id='customer' class="exercise.order.domain.Customer">
	<property name="id" value='1'/>
	<property name="name" value='홍길동'/>
	<property name="address" value='서울시'/>
	<property name="email" value='kosta@kosta.co.kr'/>
</bean>

<!-- 
	1. 여기에 빈 생성을 추가하고 컴포넌트 스캔 방식 
	2. CustomerServiceImpl에 필요한 부분을 추가
 -->
<context:component-scan base-package="exercise.order"/>
</beans>
~~~