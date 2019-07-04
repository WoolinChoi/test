---
layout: post
title: webBoard
category: spring
tags: [java, spring, webBoard]
comments: false
---

# [webBoard]()

## Servlet-context_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans:beans xmlns="http://www.springframework.org/schema/mvc"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:beans="http://www.springframework.org/schema/beans"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc.xsd
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
	<!-- DispatcherServlet Context: defines this servlet's request-processing infrastructure -->
	
	<!-- Enables the Spring MVC @Controller programming model -->
	<annotation-driven />

	<!-- Handles HTTP GET requests for /resources/** by efficiently serving up static resources in the ${webappRoot}/resources directory -->
	<resources mapping="/resources/**" location="/resources/" />

	<!-- Resolves views selected for rendering by @Controllers to .jsp resources in the /WEB-INF/views directory -->
	<beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<beans:property name="prefix" value="/WEB-INF/views/" />
		<beans:property name="suffix" value=".jsp" />
	</beans:bean>
	
	<context:component-scan base-package="com.javassem" />
</beans:beans>
~~~

## Root-context_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:mybatis-spring="http://mybatis.org/schema/mybatis-spring"
	xsi:schemaLocation="http://mybatis.org/schema/mybatis-spring http://mybatis.org/schema/mybatis-spring-1.2.xsd
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.1.xsd">
	
<!-- Root Context: defines shared resources visible to all other web components -->
<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
	<property name="driverClassName" value="oracle.jdbc.driver.OracleDriver"></property>
	<property name="url" value="jdbc:oracle:thin:@192.168.0.116:1521:orcl"></property>
	<property name="username" value="team5"></property>
	<property name="password" value="1004"></property>
</bean>	
	
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
 	<property name="dataSource" ref="dataSource" />
  <property name="configLocation" value="classpath:/mybatis-config.xml"></property>
  <property name="mapperLocations" value="classpath:mappers/**/*Mapper.xml"></property>
 </bean>
 
 <bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate" destroy-method="clearCache">
   <constructor-arg name="sqlSessionFactory" ref="sqlSessionFactory"></constructor-arg>
 </bean>
 
<!--  <context:component-scan base-package="org.javassem"></context:component-scan> -->		
</beans>
~~~

## Web_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="2.5" xmlns="http://java.sun.com/xml/ns/javaee"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">

	<!-- The definition of the Root Spring Container shared by all Servlets and Filters -->
	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/spring/root-context.xml</param-value>
	</context-param>
	
	<!-- Creates the Spring Container shared by all Servlets and Filters -->
	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>

	<!-- Processes application requests -->
	<servlet>
		<servlet-name>appServlet</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
		<init-param>
			<param-name>contextConfigLocation</param-name>
			<param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
		</init-param>
	</servlet>
		
	<servlet-mapping>
		<servlet-name>appServlet</servlet-name>
		<url-pattern>/</url-pattern>
	</servlet-mapping>
	
	<!-- 한글인코딩  -->
	  <filter>
	  	<filter-name>charEncoding</filter-name>
	  	<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
	  	<init-param>
	  		<param-name>encoding</param-name>
	  		<param-value>UTF-8</param-value>
	  	</init-param>
	  </filter>
	  <filter-mapping>
	  	<filter-name>charEncoding</filter-name>
	  	<url-pattern>/*</url-pattern>
	  </filter-mapping>  
</web-app>
~~~

## Mybatis-config_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
	<!-- Alias(별칭) 설정 -->
	<typeAliases>
		<typeAlias alias="board" type="com.javassem.domain.BoardVO" />		
	</typeAliases>
</configuration>
~~~

## MainPage
~~~jsp
<%@page contentType="text/html; charset=EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
	<title>MainPage</title>
</head>

<body>
	<h1>게시판 프로그램</h1>
	<hr/><br/>
	<a href="getBoardList.do">글 목록 바로가기</a>
	<hr/><br/>
</body>
</html>
~~~

## BoardVO
~~~java
package com.javassem.domain;
import java.util.Date;

// VO(Value Object)
public class BoardVO {

	private int seq;
	private String title;
	private String writer;
	private String content;
	private Date regDate;
	private int cnt;


	public int getSeq() {
		return seq;
	}

	public void setSeq(int seq) {
		this.seq = seq;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getWriter() {
		return writer;
	}

	public void setWriter(String writer) {
		this.writer = writer;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public Date getRegDate() {
		return regDate;
	}

	public void setRegDate(Date regDate) {
		this.regDate = regDate;
	}

	public int getCnt() {
		return cnt;
	}

	public void setCnt(int cnt) {
		this.cnt = cnt;
	}

	public String toString() {
		return "BoardVO [seq=" + seq + ", title=" + title + ", writer=" + writer + ", content=" + content + ", regDate="
				+ regDate + ", cnt=" + cnt + "]";
	}
}
~~~

## BoardController
~~~java
package com.javassem.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import com.javassem.domain.BoardVO;
import com.javassem.service.BoardService;

@Controller
public class BoardController {
	// Controller는 Service객체가 필요해서 Autowired해준다.
	@Autowired
	private BoardService boardService;
	
	// 글 목록
	@RequestMapping("/getBoardList.do")
/*
	public void getBoadrList(BoardVO vo, Model model) {
		List<BoardVO> list = boardService.getBoardList(vo); // 지금은 vo가 비어있는 상태
		// (1) Model, (2) ModelAndView, (3) 함수위에 @ModelAttribute
		model.addAttribute("boardList", list);
	} // Model은 리턴이 필요없다.
*/
	public ModelAndView getBoadrList(BoardVO vo) {
		ModelAndView mv = new ModelAndView();
		mv.addObject("boardList", boardService.getBoardList(vo));
		mv.setViewName("getBoardList");
		return mv;
	} // ModelAndView은 리턴이 필요하다.
	
	// 글 입력
	@RequestMapping("/insertBoard.do")
	public void insertBoard() {
		// 리턴형이 void이면 요청이름(insertBoard)과 동일한 뷰이름(/WEB-INF/views/ + insertBoard + .jsp)이 지정
	}
	
	// 글 등록
	@RequestMapping("/saveBoard.do")
	public String saveBoard(BoardVO vo) {
		// 이전화면 입력값인 파라메터 받기
		boardService.insertBoard(vo);
		return "redirect:getBoardList.do";
	}
	
	// 글 상세
	@RequestMapping("/getBoard.do")
	public ModelAndView getBoard(BoardVO vo) {
		ModelAndView mv = new ModelAndView();
		mv.addObject("board", boardService.getBoard(vo));
		mv.setViewName("getBoard");
		
		return mv;
	}
	
	// 글 삭제
	@RequestMapping("/deleteBoard.do")
	public String deleteBoard(BoardVO vo) {
		boardService.deleteBoard(vo);
		return "redirect:getBoardList.do";
	}
	
	// 글 수정
	@RequestMapping("/updateBoard.do")
	public String updateBoard(BoardVO vo) {
		boardService.updateBoard(vo);
		return "redirect:getBoardList.do";
	}
}
~~~

## BoardDAO
~~~java
package com.javassem.dao;
import java.util.List;
import com.javassem.domain.BoardVO;
public interface BoardDAO {
	
	public void insertBoard(BoardVO vo);

	public void updateBoard(BoardVO vo) ;

	public void deleteBoard(BoardVO vo);

	public BoardVO getBoard(BoardVO vo) ;

	public List<BoardVO> getBoardList(BoardVO vo) ;
}
~~~

## BoardDAOImpl
~~~java
package com.javassem.dao;
import java.util.List;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import com.javassem.domain.BoardVO;

@Repository("boardDAO")
public class BoardDAOImpl implements BoardDAO {
	
	@Autowired
	private SqlSessionTemplate mybatis;

	public void insertBoard(BoardVO vo) {
		System.out.println("===> Mybatis insertBoard() 호출");
		mybatis.insert("BoardDAO.insertBoard", vo);
	}

	public void updateBoard(BoardVO vo) {
		System.out.println("===> Mybatis updateBoard() 호출");
		mybatis.update("BoardDAO.updateBoard", vo);
	}

	public void deleteBoard(BoardVO vo) {
		System.out.println("===> Mybatis deleteBoard() 호출");
		mybatis.delete("BoardDAO.deleteBoard", vo);
	}

	public BoardVO getBoard(BoardVO vo) {
		System.out.println("===> Mybatis getBoard() 호출");
		mybatis.update("BoardDAO.increaseReadCount", vo);	
		return (BoardVO) mybatis.selectOne("BoardDAO.getBoard", vo);
	}

	public List<BoardVO> getBoardList(BoardVO vo) {
		System.out.println("===> Mybatis getBoardList() 호출");
		return mybatis.selectList("BoardDAO.getBoardList", vo);
	}
}
~~~

## BoardService
~~~java
package com.javassem.service;
import java.util.List;
import com.javassem.domain.BoardVO;

public interface BoardService {
	// CRUD 기능의 메소드 구현
	// 글 등록
	void insertBoard(BoardVO vo);

	// 글 수정
	void updateBoard(BoardVO vo);

	// 글 삭제
	void deleteBoard(BoardVO vo);

	// 글 상세 조회
	BoardVO getBoard(BoardVO vo);

	// 글 목록 조회
	List<BoardVO> getBoardList(BoardVO vo);
}
~~~

## BoardServiceImpl
~~~java
package com.javassem.service;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.javassem.dao.BoardDAOImpl;
import com.javassem.domain.BoardVO;

@Service("boardService")
public class BoardServiceImpl implements BoardService {
	
	@Autowired
	private BoardDAOImpl boardDAO;

	public void insertBoard(BoardVO vo) {
		boardDAO.insertBoard(vo);
	}

	public void updateBoard(BoardVO vo) {
		boardDAO.updateBoard(vo);
	}

	public void deleteBoard(BoardVO vo) {
		boardDAO.deleteBoard(vo);
	}

	public BoardVO getBoard(BoardVO vo) {
		return boardDAO.getBoard(vo);
	}

	public List<BoardVO> getBoardList(BoardVO vo) {
		return boardDAO.getBoardList(vo);
	}
}
~~~

## BoardMapper_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="BoardDAO">
	<resultMap id="boardResult" type="board">
		<id property="seq" column="SEQ" />
		<result property="title" column="TITLE" />
		<result property="writer" column="WRITER" />
		<result property="content" column="CONTENT" />
		<result property="regDate" column="REGDATE" />
		<result property="cnt" column="CNT" />
	</resultMap>
	
	<insert id="insertBoard" parameterType="board">
		<![CDATA[
		INSERT INTO BOARD(SEQ, TITLE, WRITER, CONTENT, REGDATE, CNT)
		VALUES(board_seq.nextval,
			#{title}, #{writer}, #{content}, 
			sysdate, 0)
		]]>
	</insert>
	
	<update id="updateBoard" parameterType="board">
		<![CDATA[
		UPDATE BOARD SET
		TITLE = #{title},
		CONTENT = #{content}
		WHERE SEQ = #{seq}
		]]>
	</update>
	
	<delete id="deleteBoard" parameterType="board">
		<![CDATA[
		DELETE BOARD
		WHERE SEQ = #{seq}
		]]>
	</delete>
	
	<select id="getBoard" parameterType="board" resultType="board">
		<![CDATA[
		SELECT *
		FROM BOARD
		WHERE SEQ = #{seq}
		]]>
	</select>
	
	<select id="getBoardList" parameterType="board" resultMap="boardResult">
		<![CDATA[
		SELECT *
		FROM BOARD
		ORDER BY SEQ DESC
		]]>
	</select>
	
	<update id="increaseReadCount" parameterType="board">
		<![CDATA[
		UPDATE BOARD
		SET CNT = CNT + 1
		WHERE SEQ = #{seq}
		]]>	
	</update>
</mapper>
~~~

## GetBoardList
~~~jsp
<%@ page contentType="text/html; charset=EUC-KR"%>
<%@ taglib uri="http://java.sun.com/jstl/core_rt" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>

<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
	<title>/WEB-INF/views/getBoardList.jsp</title>
</head>

<body>
	<h1>게시글 목록</h1>
	<table border="1">
		<tr>
			<th bgcolor="orange" width="100">번호</th>
			<th bgcolor="orange" width="200">제목</th>
			<th bgcolor="orange" width="150">작성자</th>
			<th bgcolor="orange" width="150">등록일</th>
			<th bgcolor="orange" width="100">조회수</th>
		</tr>
		
		<!-- items는 Controller에서 보낸 객체명과 같아야한다. -->
		<c:forEach items="${boardList}" var="board">
			<tr>
				<td>${board.seq}</td>
				<td align="left"><a href="getBoard.do?seq=${board.seq}">
						${board.title}</a></td>
				<td>${board.writer}</td>
				<td><fmt:formatDate value="${board.regDate}" pattern="yyyy-MM-dd"/></td>
				<td>${board.cnt}</td>				
			</tr>
		</c:forEach>
	</table>
	<br> <a href="insertBoard.do">새글 등록</a>
</body>
</html>
~~~

## InsertBoard
~~~jsp
<%@page contentType="text/html; charset=UTF-8"%>

<!DOCTYPE html>
<html>
<head>
	<title>/WEB-INF/views/insertBoard.jsp</title>
</head>

<body>
	<h1>글 등록</h1>		
	<hr/>
	<form action="saveBoard.do" method="post"> <!--  enctype="multipart/form-data" -->
		<table border="1" cellpadding="0" cellspacing="0">
			<tr>
				<td bgcolor="orange" width="70">제목</td>
				<td align="left"><input type="text" name="title" /></td>
			</tr>
			<tr>
				<td bgcolor="orange">작성자</td>
				<td align="left"><input type="text" name="writer" size="10" /></td>
			</tr>
			<tr>
				<td bgcolor="orange">내용</td>
				<td align="left"><textarea name="content" cols="40" rows="10"></textarea></td>
			</tr>
			<tr>
				<td colspan="2" align="center"><input type="submit"	value=" 새글 등록 " /></td>
			</tr>
		</table>
	</form>
	<hr>
	<a href="getBoardList.do">글 목록 가기</a>
</body>
</html>
~~~

## GetBoard
~~~jsp
<%@page contentType="text/html; charset=UTF-8"%>

<!DOCTYPE>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>/WEB-INF/views/getBoard.jsp</title>
</head>

<body>
	<h1>글 상세</h1>		
	<hr>
	<form action="updateBoard.do" method="post">
		<input name="seq" type="hidden" value="${board.seq}" />
		<table border="1" cellpadding="0" cellspacing="0">
			<tr>
				<td bgcolor="orange" width="70">제목</td>
				<td align="left"><input name="title" type="text"
					value="${board.title}" /></td>
			</tr>
			<tr>
				<td bgcolor="orange">작성자</td>
				<td align="left">${board.writer}</td>
			</tr>
			<tr>
				<td bgcolor="orange">내용</td>
				<td align="left"><textarea name="content" cols="40" rows="10">
					${board.content}</textarea></td>
			</tr>
			<tr>
				<td bgcolor="orange">등록일</td>
				<td align="left">${board.regDate}</td>
			</tr>
			<tr>
				<td bgcolor="orange">조회수</td>
				<td align="left">${board.cnt}</td>
			</tr>
			<tr>
				<td colspan="2" align="center"><input type="submit"
					value="글 수정" /></td>
			</tr>
		</table>
	</form>
	<hr>
	<a href="insertBoard.do">글등록</a>&nbsp;&nbsp;&nbsp; 
	<a href="deleteBoard.do?seq=${board.seq}">글삭제</a>&nbsp;&nbsp;&nbsp;
	<a href="getBoardList.do">글목록</a>
</body>
</html>
~~~