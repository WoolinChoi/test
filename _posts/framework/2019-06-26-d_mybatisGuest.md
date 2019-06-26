---
layout: post
title: mybatisGuest
category: framework
tags: [java, framework, mybatis, mybatisGuest]
comments: false
---

# [mybatisGuest]()

## listComment
~~~jsp
<%@ page language="java" contentType="text/html; charset=utf-8" %>
<%@ page import="java.util.*" %>
<%@ page import="mybatis.guest.model.Comment" %>    
<%@ page import="mybatis.guest.service.CommentService" %>  
<!-- 서비스의 메소드 호출  -->
<%
	//Map condition = new HashMap();
	List<Comment> mList = CommentService.getInstance().selectComment();
%>  
<!DOCTYPE HTML>
<html> 
<head>
	<meta charset="UTF-8">
	<title>listComment</title>
</head>

<body>
<a href="insertCommentForm.jsp">방명록 남기기</a><br/><br/>

<table border="1">
	<tr><td>글번호</td><td>작성자</td><td>등록일</td></tr>
	<% for(Comment comment : mList){ %>
		<tr>
			<td><%= comment.getCommentNo() %></td>
			<td><a href="viewComment.jsp?cId=<%= comment.getCommentNo() %>"><%= comment.getUserId() %>님이 쓴 글</a></td>
			<td><%= comment.getRegDate() %></td>
		</tr>
	<% } // for-end %>
</table>
</body>
</html>
~~~

## ViewComment
~~~jsp
<%@ page language="java" contentType="text/html; charset=utf-8"%>
<%@ page import="mybatis.guest.model.Comment" %>   
<%@ page import="mybatis.guest.service.CommentService" %>          
<!-- 키에 해당하는 글번호를 넘겨받아 서비스의 메소드 호출  -->
<% 
  long commentNo = Integer.parseInt(request.getParameter("cId"));
  Comment comment = CommentService.getInstance().selectCommentByPrimaryKey(commentNo);
%>
<!DOCTYPE HTML>
<html>
<head>
	<meta charset="UTF-8">
	<title>ViewComment</title>
	<script type="text/javascript">
		window.onload = function(){
			// 삭제를 눌렀을 때
			document.getElementById("btnDelete").onclick = function(){
				window.location.href = "deleteComment.jsp?cId=<%= comment.getCommentNo() %>";
			}
		}
	</script>
</head>

<body>
    <form name="frm" action="modityComment.jsp">
        <table border="1">
            작성자 : <input type="text" name="commentNo" value="<%= comment.getCommentNo() %>"/><br/><br/>
            메세지 : <textarea name="message" rows="3" cols="30"><%= comment.getCommentContent() %></textarea><br/><br/>
            등록일 : <input type="text" name="regDate" value="<%= comment.getRegDate() %>"/><br/><br/>
            <input type="submit" id="btnModify" value="수정" />
            <input type="button" id="btnDelete" value="삭제" />
        </table>
    </form>
</body>
</html>
~~~

## InsertCommentForm
~~~jsp
<%@ page language="java" contentType="text/html; charset=utf-8"%>
<!DOCTYPE HTML>
<html>
<head>
	<meta charset="UTF-8">
	<title>InsertCommentForm</title>
</head>

<body>
	메세지를 남겨주세요.
	<form name="frm" action="insertCommentSave.jsp" >
	<table>
		<tr><td>사용자</td><td><input type="text" name="userId" size="15"/></td></tr>
		<tr><td>메세지</td><td><textarea name="commentContent" rows="10" columns="40"></textarea></td></tr>
		<tr><td><input type="submit" value="입력"/></td></tr>
	</table>
	</form>
</body>
</html>
~~~

## InsertCommentSave
~~~jsp
<%@ page language="java" contentType="text/html; charset=utf-8"%>
<%@ page import="mybatis.guest.model.Comment" %>    
<%@ page import="mybatis.guest.service.CommentService" %>   
<!--  이전 폼에서 넘겨오는 데이타의 한글 처리  -->
<% 
	request.setCharacterEncoding("utf-8");
%>
  
<!--  이전 폼의 각각의 데이터를 빈즈의 멤버로 지정  -->
<jsp:useBean id="comment" class="mybatis.guest.model.Comment">
	<jsp:setProperty name="comment" property="*"/>
</jsp:useBean>   
 
<!-- 서비스의 메소드 호출  -->
<%
	CommentService.getInstance().insertComment(comment);
%>
<!DOCTYPE HTML>
<html>
<head>
	<meta charset="UTF-8">
	<title>InsertCommentSave</title>
</head>

<body>
	입력되었는지 확인해보세요. <br/>
	<a href="listComment.jsp">목록보기</a>
</body>
</html>
~~~

## DeleteComment
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mybatis.guest.model.Comment" %>    
<%@ page import="mybatis.guest.service.CommentService" %> 
<!-- 
	1. import
	2. 이전 화면에서 넘어오는 cId 값을 얻어오기
	3. Service에 함수를 호출
 -->
<% 
	long commentNo = Integer.parseInt(request.getParameter("cId"));
	int result = CommentService.getInstance().deleteCommentByPrimaryKey(commentNo);
%> 
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>DeleteComment</title>
</head>

<body>
	<% if(result > 0){ %> 
		삭제되었습니다.
	<% }else{ %> 
		다시 시도해주세요.
	<% } // if-end %>
	<a href="listComment.jsp">목록보기</a>
</body>
</html>
~~~

## modityComment
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mybatis.guest.model.Comment" %>    
<%@ page import="mybatis.guest.service.CommentService" %> 
<%
	// 1. 수정할 데이터를 가져온다.
	Comment c = new Comment();
	c.setCommentNo(Integer.parseInt(request.getParameter("commentNo")));
	c.setCommentContent(request.getParameter("message"));
	c.setRegDate(request.getParameter("regDate"));
	
	// 2. Service에 modifyCommentByPrimaryKey() 호출
	int result = CommentService.getInstance().modifyCommentByPrimaryKey(c);
%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>modityComment</title>
</head>
<body>
	<% if(result > 0){ %> 
		수정되었습니다.
	<% }else{ %> 
		다시 시도해주세요.
	<% } // if-end %>
	<a href="listComment.jsp">목록보기</a>	
</body>
</html>
~~~

## Comment
~~~java
package mybatis.guest.model;
import java.io.Serializable;
public class Comment implements Serializable {
	private long commentNo;
	private String userId;
	private String commentContent;
	private String regDate;
	
	public long getCommentNo() {
		return commentNo;
	}
	public void setCommentNo(long commentNo) {
		this.commentNo = commentNo;
	}
	public String getUserId() {
		return userId;
	}
	public void setUserId(String userId) {
		this.userId = userId;
	}
	public String getCommentContent() {
		return commentContent;
	}
	public void setCommentContent(String commentContent) {
		this.commentContent = commentContent;
	}
	public String getRegDate() {
		return regDate;
	}
	public void setRegDate(String regDate) {
		this.regDate = regDate;
	}
}
~~~

## MybatisConfig_xml
~~~xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
 PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
 "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
	<!-- db connect file -->
	<properties resource="db.properties"></properties>
	
	<!-- 기타설정 -->
	<settings>
		<setting name="mapUnderscoreToCamelCase" value="true"/>
	</settings>
	
	<!-- alias 별칭 -->
	<typeAliases>
		<typeAlias type="mybatis.guest.model.Comment" alias="Comment"/>
	</typeAliases>
	
	<environments default="development">
		<environment id="development">
			<transactionManager type="JDBC"/>
			<dataSource type="POOLED">
				<property name="driver" value="${driver}"/>
				<property name="url" value="${url}"/>
				<property name="username" value="${username}"/>
				<property name="password" value="${password}"/>
			</dataSource>
		</environment>
	</environments>
	
	<!-- 각각 mapper 등록 -->
	<mappers>
		<mapper resource="mybatis/guest/mapper/CommentMapper.xml"/>
	</mappers>
</configuration>
~~~

## DBconnectInfo
~~~s
# db connect info
driver=oracle.jdbc.driver.OracleDriver
url=jdbc:oracle:thin:@192.168.0.116:1521:orcl
username=team5
password=1004
~~~

## CommentMapper_xml
~~~xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
 PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
 "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="mapper.CommentMapper">
	<select id="selectComment" parameterType="hashmap" resultType="Comment">
		SELECT * 
		FROM comment_tab
		<where>
			<!-- <![CDATA[comment_no >= 20]]> -->
			<if test="commentNo != null">
				comment_no=#{commentNo}
			</if>
		</where>
	</select>
	
<!-- 	<select id="selectCommentByPK" parameterType="long" resultType="Comment"> -->
<!-- 		SELECT *  -->
<!-- 		FROM comment_tab  -->
<!-- 		WHERE comment_no=#{commentNo} -->
<!-- 	</select> -->
	
	<insert id="insertComment" parameterType="Comment">
		INSERT INTO comment_tab(comment_no, user_id, comment_content, reg_date) 
		VALUES (seq_comment_no.nextval, #{userId}, #{commentContent}, sysdate)
	</insert>
	
	<delete id="deleteCommentByPK" parameterType="long">
		DELETE FROM comment_tab 
		WHERE comment_no=#{commentNo}
	</delete>
	
	<update id="modifyCommentByPK" parameterType="long">
		UPDATE comment_tab 
		SET comment_content=#{commentContent}
		WHERE comment_no=#{commentNo}
	</update>
</mapper>
~~~

## CommentRepository
~~~java
package mybatis.guest.session;
import java.io.InputStream;
import java.util.*;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.*;
import mybatis.guest.model.Comment;
public class CommentRepository {
	String namespace = "mapper.CommentMapper";
	
	SqlSessionFactory getSqlSessionFactory() {
		InputStream inStream = null;
		
		try {
			inStream = Resources.getResourceAsStream("mybatis-config.xml");
		}catch(Exception ex) {
			System.out.println("config 파일 연결 실패: " + ex.getMessage());
		}
		
		SqlSessionFactory sessFactory = new SqlSessionFactoryBuilder().build(inStream);
		return sessFactory;
	}
	
	// 방명록 전체 검색
	public List<Comment> selectComment(){
		// mybatis가 관리는 Connection 하나를 얻어오기 - Connection 개념 -> SqlSeesion
		SqlSession sess = getSqlSessionFactory().openSession();
		try {
//			return sess.selectList("mapper.CommentMapper.selectComment");
			return sess.selectList(namespace + ".selectComment");
		}finally {
			sess.close(); // Connection mybatis에게 반환
		}
	}
	
	// 방명록 글 번호로 검색
	public Comment selectCommentByPK(long commentNo) {
		SqlSession sess = getSqlSessionFactory().openSession();
		try {
			// 쿼리문에 ?가 있으면 ?는 commentNo로 하겠다 이때, selectComment에서 commentNo를 찾는다. 
			Map map = new HashMap();
			map.put("commentNo", commentNo);
			Comment c = sess.selectOne(namespace + ".selectComment", map);
			return c;
		}finally {
			sess.close();
		}
	}
	
	// 방명록 입력
	public void insertComment(Comment c) {
		SqlSession sess = getSqlSessionFactory().openSession();
		try {
			// 입력됬다는 값을 result로 받아 if문으로 commit과 rollback해준다.
			int result = sess.insert(namespace + ".insertComment", c);
			if(result > 0) {
				sess.commit();
			}else {
				sess.rollback();
			}
		}finally {
			sess.close();
		}
	}
	
	// 글 번호로 방명록 삭제
	public int deleteCommentByPK(long commentNo) {
		SqlSession sess = getSqlSessionFactory().openSession();
		try {
			int result = sess.delete(namespace + ".deleteCommentByPK", commentNo);
			if(result > 0) {
				sess.commit();
			}else {
				sess.rollback();
			}
			return result;
		}finally {
			sess.close();
		}
	}
	
	// 글 번호로 방명록 수정
	public int modifyCommentByPK(Comment c) {
		SqlSession sess = getSqlSessionFactory().openSession();
		try {
			int result = sess.delete(namespace + ".modifyCommentByPK", c);
			if(result > 0) {
				sess.commit();
			}else {
				sess.rollback();
			}
			return result;
		}finally {
			sess.close();
		}
	}
}
~~~

## CommentService
~~~java
package mybatis.guest.service;
import java.util.List;
import mybatis.guest.model.Comment;
import mybatis.guest.session.CommentRepository;
public class CommentService {
	private static CommentService service;
	
	private CommentService() {}
	
	public static CommentService getInstance() {
		if(service == null) {
			service = new CommentService();
		}
		return service;
	}
	
	CommentRepository repo = new CommentRepository();
	// 방명록 전체 검색
	public List<Comment> selectComment(){
		return repo.selectComment();
	}
	
	// 방명록 글 번호로 검색(return 값의 자료형은 Comment)
	public Comment selectCommentByPrimaryKey(long cId) {
		return repo.selectCommentByPK(cId);
	}
	
	// 방명록 입력(return값이 필요없기 때문에 void)
	public void insertComment(Comment c) {
		repo.insertComment(c);
	}
	
	// 글 번호로 방명록 삭제(return 값의 자료형은 int)
	public int deleteCommentByPrimaryKey(long cId) {
		return repo.deleteCommentByPK(cId);
	}
	
	// 글 번호로 방명록 수정(return 값의 자료형은 int)
	public int modifyCommentByPrimaryKey(Comment c){
		return repo.modifyCommentByPK(c);
	}
}
~~~

## Log4j_xml
~~~xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE log4j:configuration SYSTEM "http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/xml/doc-files/log4j.dtd">
<log4j:configuration xmlns:log4j="http://jakarta.apache.org/log4j/">
	<appender name="console" class="org.apache.log4j.ConsoleAppender">
		<layout class="org.apache.log4j.PatternLayout">
			<param name="ConversionPattern" value="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-35c{1}:%-3L) %m%n" />
		</layout>
	</appender>
	
	<root>
		<level value="DEBUG" />
		<appender-ref ref="console" />
	</root>
</log4j:configuration>
~~~