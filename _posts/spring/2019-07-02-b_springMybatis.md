---
layout: post
title: springMybatis
category: spring
tags: [java, spring, springMybatis]
comments: false
---

# [springMybatis]()

## MainApp
~~~java
import java.util.List;
import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;
import board.BoardService;
import board.BoardVO;
public class MainApp {
	public static void main(String[] args) {
		// 1. Spring 컨테이너를 구동한다.
		AbstractApplicationContext container = new GenericXmlApplicationContext("applicationContext.xml");

		// 2. Spring 컨테이너로부터 BoardServiceImpl 객체를 Lookup한다.
		BoardService boardService = (BoardService) container.getBean("boardService");

		// 3. 글 등록 기능 테스트
//		BoardVO vo = new BoardVO();
//		vo.setTitle("spring mybatis");
//		vo.setWriter("홍길동S");
//		vo.setContent("임시 내용..............");
//		boardService.insertBoard(vo);

		// 4. 글 목록 검색 기능 테스트		
		BoardVO svo = new BoardVO();
		List<BoardVO> boardList = boardService.getBoardList(svo);
		for (BoardVO board : boardList) {
			System.out.println("---> " + board.toString());
		}

		// 5. Spring 컨테이너 종료
		container.close();
	}
}
~~~

## BoardService
~~~java
package board;
import java.util.List;
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

## BoardVO
~~~java
package board;
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

## BoardDAOMybatis
~~~java
package board.impl;
import java.util.List;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import board.BoardVO;

@Repository
public class BoardDAOMybatis {

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
		return (BoardVO) mybatis.selectOne("BoardDAO.getBoard", vo);
	}

	public List<BoardVO> getBoardList(BoardVO vo) {
		System.out.println("===> Mybatis getBoardList() 호출");
		return mybatis.selectList("BoardDAO.getBoardList", vo);
	}
}
~~~

## BoardServiceImpl
~~~java
package board.impl;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import board.BoardService;
import board.BoardVO;

@Service("boardService")
public class BoardServiceImpl implements BoardService {
	
	@Autowired
	private BoardDAOMybatis boardDAO;

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

## Board-mapping_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="BoardDAO">
	<!-- 
		조인할 때 2개 이상의 테이블의 컬럼을 받아 올 때 필요 할 수 있음(자주사용시)
		조인 시 resultType="hashmap"으로 하면 resultMap 필요없음 
	-->
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
	
	<update id="updateBoard">
		<![CDATA[
		UPDATE BOARD SET
		TITLE = #{title},
		CONTENT = #{content}
		WHERE SEQ = #{seq}
		]]>
	</update>
	
	<delete id="deleteBoard">
		<![CDATA[
		DELETE BOARD
		WHERE SEQ = #{seq}
		]]>
	</delete>
	
	<select id="getBoard" resultType="board">
		<![CDATA[
		SELECT *
		FROM BOARD
		WHERE SEQ = #{seq}
		]]>
	</select>
	
	<select id="getBoardList" resultMap="boardResult">
		<![CDATA[
		SELECT *
		FROM BOARD
		ORDER BY SEQ DESC
		]]>
	</select>
</mapper>
~~~

## mybatis-config_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>	
	<!-- Alias 설정 -->
	<typeAliases>
		<typeAlias alias="board" type="board.BoardVO" />
	</typeAliases>
	
	<!-- Sql Mapper 설정 -->
	<mappers>
		<mapper resource="mappings/board-mapping.xml" />
	</mappers>
</configuration>
~~~

## ApplicationContext_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.2.xsd">
<!-- 빈 객체 생성  -->
<context:component-scan base-package="board.impl"></context:component-scan>

<!-- DataSource 설정 -->
<context:property-placeholder location="classpath:config/database.properties"/>
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
	<!-- setDriverClassName() -->
	<property name="driverClassName" value="${jdbc.driver}"/> 
	<property name="url" value="${jdbc.url}"/>
	<property name="username" value="${jdbc.username}"/>
	<property name="password" value="${jdbc.password}"/>
</bean>

<!-- Spring과 Mybatis 연동 설정 -->
<!-- ref는 bean 객체를 쓸 때이고 value는 값을 쓸 때이다 -->
<bean id="sqlSession" class="org.mybatis.spring.SqlSessionFactoryBean">
	<property name="dataSource" ref="dataSource"/>
	<property name="configLocation" value="classpath:mybatis-config.xml"/>
</bean>

<!-- 생성한 SqlSession을 Template를 해주어 SQL 실행이나 트랜잭션을 관리를 실행한다 -->
<bean class="org.mybatis.spring.SqlSessionTemplate">
	<constructor-arg ref="sqlSession"/>
</bean>
</beans>
~~~