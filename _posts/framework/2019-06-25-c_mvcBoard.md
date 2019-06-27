---
layout: post
title: mvcBoard
category: framework
tags: [java, framework, mvc, mvcBoard]
comments: false
---

# [mvcBoard]()

## Main
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% String projectName = "/Test"; %>    
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Main</title>
</head>

<body>
	<a href="<%= projectName %>/board?cmd=main-page"> 메인 </a><br/><br/>
	<a href="<%= projectName %>/board?cmd=list-page"> 게시판 </a><br/><br/>
</body>
</html>
~~~

## BoardList
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" %>
<%@ page import="java.util.List" %>
<%@ page import="mvc.board.model.*" %>
<%
	int pCount = (int)request.getAttribute("pCount");
	List <BoardRec> mList = (List<BoardRec>)request.getAttribute("mList");
%>  
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>BoardList</title>
</head>

<body>
	<h3> 게시판 목록 </h3>
	<table border="1" bordercolor="darkblue">
		<tr>
			<td> 글번호 </td>
			<td> 제 목 </td>
			<td> 작성자 </td>
			<td> 작성일 </td>
			<td> 조회수 </td>
		</tr>
	<% if(mList.isEmpty()){ %>
		<tr>
			<td colspan="5"> 등록된 게시물이 없습니다. </td>
		</tr>
	<% }else{ %>
		<% 
// 			for(int i = 0; i < mList.size(); i++){
// 			BoardRec rec = (BoardRec)mList.get(i);
			// 향상된 for문은 콜렉션, 데이터집합, 제너릭스가 완벽할때 쓴다.
			for(BoardRec rec : mList){
		%>
		<tr>
			<td><%= rec.getArticleId() %></td>
			<td>
			<% for(int i = 0; i < rec.getLevel(); i++){ %> 
			&nbsp; 
			<% } // for-end%>
			<% if(rec.getLevel() > 0){ %>
				<img alt="" src="./imgs/board_re.gif">
			<% } // if-end %>
				<a href="board?cmd=view-page&article_id=<%= rec.getArticleId() %>"><%= rec.getTitle() %></a>
			</td>
			<td><%= rec.getWriterName() %></td>		
			<td><%= rec.getPostingDate() %></td>
			<td><%= rec.getReadCount() %></td>
		</tr>
		<% } // for-end %>
	<% } // else-end %>
		<tr>
			<td colspan="5">
				<a href="board?cmd=input-page">글쓰기</a><br/>
				<!-- 페이지 번호 출력 -->
				<% for(int i = 1; i <= pCount; i++){ %>
					<!-- 숫자에 현재 페이지로 링크를 걸어서 page 파라메타로 전송하기 -->
					<a href="board?cmd=list-page&page=<%= i %>">[<%= i %>]</a>
				<% } // for-end %>	
			</td>
		</tr>
	</table>
</body>
</html>
~~~

## BoardInputForm
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>BoardInputForm</title>
</head>

<body>
	<h4> 게시판 글 쓰기 </h4><br/>
	나중에 이쁘게 만드시오 <br/><br/>
	<form name='frm' method='post' action="board?cmd=input-do">
		작성자 : <input type='text' name='writerName'><br/><br/>
		제  목 : <input type='text' name='title'><br/><br/>
		내  용 : <textarea rows='10' cols='40' name='content'></textarea><br/><br/>
		패스워드(수정/삭제시 필요) : <input type='password' name='password'><br/><br/>
		<input type='submit' value='작성'>
		<input type='reset' value='취소'>
	</form>
</body>
</html>
~~~

## BoardSave
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>BoardSave</title>
</head>

<body>
	<font size="3" color="#bb44cc">
		게시물을 남겼습니다. 
	</font><br/><br/><br/>
	<a href="board?cmd=list-page"> [ 목록보기 ] </a>
</body>
</html>
~~~

## BoardView
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mvc.board.model.*" %>
<%
	BoardRec rec = (BoardRec)request.getAttribute("rec");
%>   
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>BoardView</title>
</head>

<body>
	<h4> 게시판 글 보기 </h4><br/>
		<table border="1" bordercolor="red">
	<tr>
		<td> 제  목 : </td>
		<td><%= rec.getTitle() %></a></td>
	</tr>
	<tr>
		<td> 작성자 : </td>
		<td><%= rec.getWriterName() %></td>
	</tr>
	<tr>
		<td> 작성일자 : </td>
		<td><%= rec.getPostingDate() %></td>
	</tr>
	<tr>
		<td> 내  용 : </td>
		<td><%= rec.getContent() %></td>
	</tr>
	<tr>
		<td> 조회수 : </td>
		<td><%= rec.getReadCount() %></td>
	</tr>
	<tr>
		<td colspan="2">
			<a href="board?cmd=list-page">목록보기</a>
			<a href="board?cmd=reply-page&parent_id=<%= rec.getArticleId() %>">답변하기</a>
			<a href="board?cmd=modify-page&modify_id=<%= rec.getArticleId() %>">수정하기</a>		
			<a href="board?cmd=delete-page&article_id=<%= rec.getArticleId() %>">삭제하기</a> 	
		</td>
	</tr>
	</table>
</body>
</html>
~~~

## BoardDeleteForm
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mvc.board.model.*" %>
<%
	String article_id = request.getParameter("article_id");
%>      
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>BoardDeleteForm</title>
</head>

<body>
	<form method="post" action="board?cmd=delete-do">
		삭제할 글암호를 입력하세요 <br/>
		<input type="password" name="password">
		
		<!-- 게시글번호를 다음 페이지로 넘기기 위해 hidden 태그로 지정 -->
		<input type="hidden" name="article_id" value="<%= article_id %>">
		<input type="submit" value="삭제하기">
	</form>
</body>
</html>
~~~

## BoardDelete
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mvc.board.model.*" %>
<%
	int result = (int)request.getAttribute("result");
%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>BoardDelete</title>
</head>

<body>
	<% if(result != 0){ %>
			글을 삭제하였습니다.
	<% }else{ %>
			삭제가 실패되었습니다.
	<% } %>
	<br/><br/>
	<a href="board?cmd=list-page"> 목록보기 </a>
</body>
</html>
~~~

## BoardModifyForm
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mvc.board.model.*" %>
<%
	String modify_id = request.getParameter("modify_id");
%>      
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>BoardModifyForm</title>
</head>

<body>
	<h4> 게시판 글 수정하기 </h4><br/>
	<form name='frm' method='post' action='board?cmd=modify-do'>
		<input type='hidden' name='articleId' value='<%= modify_id %>'>
		제  목 : <input type='text' name='title'><br/><br/>
		패스워드(수정/삭제시 필요) : <input type='password' name='password'><br/><br/>
		내  용 : <textarea rows='10' cols='40' name='content'></textarea><br/><br/>
		<input type='submit' value='수정하기'>
		<input type='button' value='목록보기' onclick="window.location='board?cmd=list-page'">
	</form>
</body>
</html>
~~~

## BoardModify
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mvc.board.model.*" %>
<%
	int result = (int)request.getAttribute("result");
	BoardRec rec = (BoardRec)request.getAttribute("rec");
%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>BoardModify</title>
</head>

<body>
	<% if(result != 0){  // 게시글 수정이 성공적으로 되었다면 그 해당 게시글을 보여주는 페이지로 이동하고 
			response.sendRedirect("board?cmd=view-page&article_id=" + rec.getArticleId()); 
	 }else{ // 그렇지 않다면, "암호가 잘못 입력되었습니다"를 출력  %> 
			암호가 잘못 입력되었습니다.
	 <% } %>
</body>
</html>
~~~

## BoardReplyForm
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String parent_id = request.getParameter("parent_id");
%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>BoardReplyForm</title>
</head>
 <body>
	<h4> 답변 글 쓰기 </h4><br/>
	<form name='frm' method='post' action='board?cmd=reply-do'>
		<input type='hidden' name='parentId' value='<%= parent_id %>'>
		작성자 : <input type='text' name='writerName'><br/><br/>
		제  목 : <input type='text' name='title'><br/><br/>
		내  용 : <textarea rows='10' cols='40' name='content'></textarea><br/><br/>
		패스워드(수정/삭제시 필요) : <input type='password' name='password'><br/><br/>
		<input type='submit' value='작성'>
		<input type='reset' value='취소'>
	</form>
</body>
</html>
~~~

## BoardReply
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mvc.board.model.*" %>
<%
	BoardRec reRec = (BoardRec)request.getAttribute("rec");
%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>BoardReply</title>
</head>

<body>
	답변글을 등록하였습니다. <br/><br/>
	<a href="board?cmd=list-page"> 목록보기 </a> &nbsp;
	<a href="board?cmd=view-page&id=<%= reRec.getArticleId() %>"> 게시글 읽기 </a>
</body>
</html>
~~~

## BoardRec
~~~java
ackage mvc.board.model;
public class BoardRec {
	// member field
	private	int		articleId;		// 게시글번호
	private	int		groupId;		// 그룹번호
	private	String	sequenceNo;		// 순서번호
	private	String	postingDate;	// 게시글등록일시
	private	int		readCount;		// 조회수
	private	String	writerName;		// 사용자이름
	private	String	password;		// 비밀번호
	private	String	title;			// 제목
	private	String	content;		// 내용
	
	
	// constructor method 
	public BoardRec() {}
	
	public BoardRec(int articleId,  int groupId, String sequenceNo, String postingDate, int readCount, String writerName, String password, String title,  String content) {
		this.articleId		= articleId;
		this.groupId		= groupId;
		this.sequenceNo		= sequenceNo;
		this.postingDate	= postingDate;
		this.readCount 		= readCount;
		this.writerName		= writerName;
		this.password		= password;
		this.title			= title;
		this.content		= content;
	}
	
	// setter
	public void setArticleId(int articleId) {	
		this.articleId = articleId;		
	}
	public void setGroupId(int groupId) {
		this.groupId = groupId;
	}
	public void setSequenceNo(String sequenceNo) {
		this.sequenceNo = sequenceNo;
	}	
	public void setPostingDate(String postingDate) {
		this.postingDate = postingDate;
	}
	public void setReadCount(int readCount) {
		this.readCount = readCount;
	}
	public void setWriterName(String writerName) {
		this.writerName = writerName;
	}	
	public void setPassword(String password) {
		this.password = password;
	}	
	public void setTitle(String title) {
		this.title = title;
	}
	public void setContent(String content) {
		this.content = content;
	}	
	
	// getter
	public int getArticleId() {
		return articleId;
	}
	public int getGroupId() {
		return groupId;
	}
	public String getSequenceNo() {
		return sequenceNo;
	}
	public String getPostingDate() {
		return postingDate;
	}
	public int getReadCount() {
		return readCount;
	}
	public String getWriterName() {
		return writerName;
	}
	public String getPassword() {
		return password;
	}
	public String getTitle() {
		return title;
	}
	public String getContent() {
		return content;
	}	

	public int getLevel() {
		if(sequenceNo == null) {return -1;}
		if(sequenceNo.length() != 16) {return -1;}
		if(sequenceNo.endsWith("999999")) {return 0;}
		if(sequenceNo.endsWith("9999")) {return 1;}
		if(sequenceNo.endsWith("99")) {return 2;}
		return 3;
	}
}
/*
	[ 참고 ]
	@ postingDate 가 실제 DB에서는 Date 형이지만, 날짜 값을 출력만 하기에 
	 Date 형이 아닌 String  형으로 받아도 된다.
	 나중에 날짜값을 사용할 일이 있으면 Date 형으로 변경 
 
*/
~~~

## BoardException
~~~java
package mvc.board.model;
public class BoardException extends Exception {
  public BoardException() {
  		super();
  	}
  	
  public BoardException(String error) {
  		super(error);
  	}
}
~~~

## BoardDao
~~~java
package mvc.board.model;
import java.sql.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
public class BoardDao {
	// Single Pattern 
	private static BoardDao instance;
	
	// DB 연결시  관한 변수 
	private static final String 	dbDriver	=	"oracle.jdbc.driver.OracleDriver";
	private static final String		dbUrl		=	"jdbc:oracle:thin:@192.168.0.117:1521:orcl";
	private static final String		dbUser		=	"jink";
	private static final String		dbPass		=	"1234";
	
	private Connection	 		con;	
	
	//--------------------------------------------
	// ##### 객체 생성하는 메소드 
	public static BoardDao getInstance() throws BoardException {
		if(instance == null) {
			instance = new BoardDao();
		}
		return instance;
	}
	
	private BoardDao() throws BoardException {
		try {
			/********************************************
				1. 오라클 드라이버를 로딩
					( DBCP 연결하면 삭제할 부분 )
			*/
			Class.forName( dbDriver );	
		}catch(Exception ex) {
			throw new BoardException("DB 연결시 오류  : " + ex.toString());	
		}
	}
	
	//--------------------------------------------
	// ##### 게시글 입력전에 그 글의 그룹번호를 얻어온다
	public int getGroupId() throws BoardException {
		PreparedStatement ps = null;
		ResultSet rs = null;
		int groupId = 1;
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
						
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "SELECT SEQ_GROUP_ID_ARTICLE.nextval GROUP_ID FROM dual";
						
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
			
			// ####[3] sql 전송
			rs = ps.executeQuery();
			
			// ####[4] 결과받기
			if(rs.next()) {
				groupId = rs.getInt("GROUP_ID");
			}
			
			return groupId;
		}catch(Exception ex) {
			throw new BoardException("게시판 ) 게시글 입력 전에 그룹번호 얻어올 때  : " + ex.toString());	
		}finally {
			if(ps   != null) {try {ps.close();}catch(SQLException ex) {}}
			if(con  != null) {try {con.close();}catch(SQLException ex) {}}
		}		
	}

	//--------------------------------------------
	// ##### 게시판에 글을 입력시 DB에 저장하는 메소드 
	public int insert(BoardRec rec) throws BoardException {
		ResultSet rs = null;
		Statement stmt	= null;
		PreparedStatement ps = null;
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
						
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "INSERT INTO ARTICLE(ARTICLE_ID, GROUP_ID, SEQUENCE_NO, POSTING_DATE, READ_COUNT, WRITER_NAME, PASSWORD, TITLE, CONTENT) " + 
					" VALUES (SEQ_ARTICLE_ID_ARTICLE.nextval, ?, ?, sysdate, 0, ?, ?, ?, ?)";
						
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
			ps.setInt(1, rec.getGroupId());
			ps.setString(2, rec.getSequenceNo());
			ps.setString(3, rec.getWriterName());
			ps.setString(4, rec.getPassword());
			ps.setString(5, rec.getTitle());
			ps.setString(6, rec.getContent());
			
			// ####[3] sql 전송
			int result = ps.executeUpdate();
			if(result > 0) {
				stmt = con.createStatement();
				rs = stmt.executeQuery("SELECT SEQ_ARTICLE_ID_ARTICLE.currval FROM dual");
				if(rs.next()) {
					return rs.getInt(1); // 첫번째 컬럼
				}
			}
			
			return -1;
		}catch(Exception ex) {
			throw new BoardException("게시판 ) DB에 입력시 오류  : " + ex.toString());	
		}finally {
			if(rs   != null) {try {rs.close();}catch(SQLException ex) {}}
			if(stmt != null) {try {stmt.close();}catch(SQLException ex) {}}
			if(ps   != null) {try {ps.close();}catch(SQLException ex) {}}
			if(con  != null) {try {con.close();}catch(SQLException ex) {}}
		}
		
	}

	//--------------------------------------------
	// ##### 전체 레코드를 검색하는 함수
	// 리스트에 보여줄거나 필요한 컬럼 : 게시글번호, 그룹번호, 순서번호, 게시글등록일시, 조회수, 작성자이름,  제목
	//							( 내용, 비밀번호  제외 )
	// 순서번호(sequence_no)로 역순정렬
	public List<BoardRec> selectList() throws BoardException {
		PreparedStatement ps = null;
		ResultSet rs = null;
		List<BoardRec> mList = new ArrayList<BoardRec>();
		boolean isEmpty = true;
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
												
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "SELECT ARTICLE_ID, GROUP_ID, SEQUENCE_NO, POSTING_DATE, READ_COUNT, WRITER_NAME, TITLE " +
					" FROM ARTICLE ORDER BY SEQUENCE_NO DESC";
												
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
									
			// ####[3] sql 전송
			rs = ps.executeQuery();
			
			// ####[4] 결과보기
			while(rs.next()) {
				BoardRec rec = new BoardRec();
				rec.setArticleId(rs.getInt("ARTICLE_ID"));
				rec.setGroupId(rs.getInt("GROUP_ID"));
				rec.setSequenceNo(rs.getString("SEQUENCE_NO"));
				rec.setPostingDate(rs.getString("POSTING_DATE"));
				rec.setReadCount(rs.getInt("READ_COUNT"));
				rec.setWriterName(rs.getString("WRITER_NAME"));
				rec.setTitle(rs.getString("TITLE"));
				
				mList.add(rec);
				isEmpty = false;
			}
			if(isEmpty) return Collections.emptyList();
			
			return mList;
		}catch(Exception ex) {
			throw new BoardException("게시판 ) DB에 목록 검색시 오류  : " + ex.toString());	
		}finally {
			if(rs   != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}		
	}
	
	//--------------------------------------------
	// ##### 현재 페이지에 보여울 게시판 목록  얻어올 때 
	public List<BoardRec> selectList(int startRow, int endRow) throws BoardException {
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		List<BoardRec> mList = new ArrayList<BoardRec>();
		boolean isEmpty = true;
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
									
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "SELECT A.ARTICLE_ID, A.TITLE, A.WRITER_NAME, A.POSTING_DATE, A.READ_COUNT " + 
					"FROM (SELECT ROW_NUMBER() OVER(ORDER BY ARTICLE_ID DESC) RNUM, ARTICLE_ID, TITLE, WRITER_NAME, POSTING_DATE, READ_COUNT FROM ARTICLE) A " + 
					"WHERE A.RNUM BETWEEN ? AND ?";
						
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
			ps.setInt(1, startRow);
			ps.setInt(2, endRow);
									
			// ####[3] sql 전송
			rs = ps.executeQuery();
			while(rs.next()) {
				// 각 컬럼들의 값을 가져와서 Message의 property로 지정, 그  Message 객체를 ArrayList에 추가
				BoardRec rec = new BoardRec();
				rec.setArticleId(rs.getInt("ARTICLE_ID"));
				rec.setTitle(rs.getString("TITLE"));
				rec.setWriterName(rs.getString("WRITER_NAME"));
				rec.setPostingDate(rs.getString("POSTING_DATE"));
				rec.setReadCount(rs.getInt("READ_COUNT"));
				
				mList.add(rec);
				isEmpty = false;
			}
			
			if(isEmpty) return Collections.emptyList();
			
			return mList;
		}catch(Exception ex) {
			throw new BoardException("방명록 ) DB에 목록 검색시 오류  : " + ex.toString());	
		}finally {
			if(rs != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con != null) {try {con.close();} catch(SQLException ex) {}}
		}		
	}

	//--------------------------------------------
	// ##### 게시물 전체 레코드 수를 검색
	public int getTotalCount() throws BoardException {
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		int count = 0;

		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
									
			// ####[1] sql 문장 만들기
			String sql = "SELECT count(*) cnt FROM ARTICLE";
									
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
									
			// ####[3] sql 전송
			rs = ps.executeQuery();
			
			// ####[4] 결과받기
			if(rs.next()) {
				count = rs.getInt("CNT");
			}
			
			return  count;
		}catch(Exception ex) {
			throw new BoardException("방명록 ) DB에 목록 검색시 오류  : " + ex.toString());	
		}finally {
			if(rs != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con != null) {try {con.close();} catch(SQLException ex) {}}
		}			
	}
	
	//--------------------------------------------
	// ##### 게시글번호에 의한 레코드 검색하는 함수
	public BoardRec selectById(int id) throws BoardException {
		PreparedStatement ps = null;
		ResultSet rs = null;
		BoardRec rec = new BoardRec();
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
									
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "SELECT * FROM ARTICLE WHERE ARTICLE_ID = ?";
									
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
			ps.setInt(1, id);
						
			// ####[3] sql 전송
			rs = ps.executeQuery();
			
			// ####[4] 결과보기
			if(rs.next()) {
				rec.setArticleId(rs.getInt("ARTICLE_ID"));
				rec.setGroupId(rs.getInt("GROUP_ID"));
				rec.setSequenceNo(rs.getString("SEQUENCE_NO"));
				rec.setPostingDate(rs.getString("POSTING_DATE"));
				rec.setReadCount(rs.getInt("READ_COUNT"));
				rec.setWriterName(rs.getString("WRITER_NAME"));
				rec.setTitle(rs.getString("TITLE"));
				rec.setContent(rs.getString("CONTENT"));
			}

			return rec;
		}catch(Exception ex) {
			throw new BoardException("게시판 ) DB에 글번호에 의한 레코드 검색시 오류  : " + ex.toString());	
		}finally {
			if(rs   != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}		
	}

	//--------------------------------------------
	// ##### 게시글 보여줄 때 조회수 1 증가
	public void increaseReadCount(int article_id) throws BoardException {
		PreparedStatement ps = null;
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
												
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "UPDATE ARTICLE SET READ_COUNT = READ_COUNT + 1 WHERE ARTICLE_ID = ?";
												
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
			ps.setInt(1, article_id);
									
			// ####[3] sql 전송
			ps.executeUpdate();

		}catch(Exception ex) {
			throw new BoardException("게시판 ) 게시글 볼 때 조회수 증가시 오류  : " + ex.toString());	
		}finally {
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}	
	}
	
	//--------------------------------------------
	// ##### 게시글 수정할 때
	//		 (게시글번호와 패스워드에 의해 수정)
	public int update(BoardRec rec) throws BoardException {
		PreparedStatement ps = null;
		int result = 0;
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
															
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "UPDATE ARTICLE SET TITLE=?, CONTENT=? WHERE ARTICLE_ID = ? AND PASSWORD = ?";
															
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
			ps.setString(1, rec.getTitle());
			ps.setString(2, rec.getContent());
			ps.setInt(3, rec.getArticleId());
			ps.setString(4, rec.getPassword());
												
			// ####[3] sql 전송
			result = ps.executeUpdate();

			return result;
		}catch(Exception ex) {
			throw new BoardException("게시판 ) 게시글 수정시 오류  : " + ex.toString());	
		}finally {
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}
	}
	
	//--------------------------------------------
	// ##### 게시글 삭제할 때
	//		 (게시글번호와 패스워드에 의해 삭제)
	public int delete(int article_id, String password) throws BoardException {
		PreparedStatement ps = null;
		int result = 0;
		
		try {
			// ####[0] 연결 객체 얻어오기
			con = DriverManager.getConnection(dbUrl, dbUser, dbPass);
												
			// ####[1] sql 문장 만들기 (insert문)
			String sql = "DELETE FROM ARTICLE WHERE ARTICLE_ID = ? AND PASSWORD = ?";
												
			// ####[2] sql 전송 객체 만들기
			ps = con.prepareStatement(sql);
			ps.setInt(1, article_id);
			ps.setString(2, password);
												
			// ####[3] sql 전송
			result = ps.executeUpdate();

			return result;	
		}catch(Exception ex) {
			throw new BoardException("게시판 ) 게시글 수정시 오류  : " + ex.toString());	
		}finally {
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}
		
	}
	
	//----------------------------------------------------
	// ##### 부모레코드의 자식레코드 중 마지막 레코드의 순서번호를 검색
	//       (제일 작은 번호값이 마지막값임)
	public String selectLastSequenceNumber(String maxSeqNum, String minSeqNum) throws BoardException {
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			con	= DriverManager.getConnection( dbUrl, dbUser, dbPass );
			String sql = "SELECT min(SEQUENCE_NO) as minseq FROM ARTICLE WHERE SEQUENCE_NO < ? AND SEQUENCE_NO >= ?";  
			ps = con.prepareStatement(sql);
			ps.setString(1, maxSeqNum);
			ps.setString(2, minSeqNum);
			rs = ps.executeQuery();
			if(!rs.next()) {				
				return null;
			}
			
			return rs.getString("minseq");
		}catch(Exception ex) {
			throw new BoardException("게시판 ) 부모와 연관된 자식 레코드 중 마지막 순서번호 얻어오기  : " + ex.toString());	
		} finally{
			if(rs   != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}			
	}
}
~~~

## BoardControl
~~~java
package mvc.board.control;
import java.io.IOException;
import java.util.HashMap;
import javax.servlet.*;
import javax.servlet.http.*;
import mvc.board.command.*;
public class BoardControl extends HttpServlet {
	private HashMap commandMap;
	private String	testDir = "/05_mvc_class/2_mvcBoard/";
	private String  error = "error.jsp";

	public BoardControl() {
        super();       
		initCommand();
	}

	private void initCommand() {
		commandMap = new HashMap();
		
		commandMap.put("main-page",	new CommandNull("Main.jsp"));
		commandMap.put("list-page",	new CommandList("BoardList.jsp"));
		commandMap.put("view-page", new CommandView("BoardView.jsp"));
		
		commandMap.put("input-page", new CommandNull("BoardInputForm.jsp"));
		commandMap.put("input-do", new CommandInput("BoardSave.jsp"));
		
		commandMap.put("delete-page", new CommandNull("BoardDeleteForm.jsp"));
		commandMap.put("delete-do", new CommandDelete("BoardDelete.jsp"));
		
		commandMap.put("modify-page", new CommandNull("BoardModifyForm.jsp"));
		commandMap.put("modify-do", new CommandModify("BoardModify.jsp"));
		
		commandMap.put("reply-page", new CommandNull("BoardReplyForm.jsp"));
		commandMap.put("reply-do", new CommandReply("BoardReply.jsp"));
	}

	public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		processRequest(request, response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		processRequest(request, response);
	}
		

	private void processRequest(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");

		String nextPage = "";
		String cmdKey = request.getParameter("cmd");
		if(cmdKey == null) {
			cmdKey = "main-page";
		}

		Command cmd = null;
		try {
			if(commandMap.containsKey(cmdKey)) {
				cmd = (Command)commandMap.get(cmdKey);
			}else {
				throw new CommandException("지정할 명령어가 존재하지 않음");
			}
			nextPage = cmd.execute(request, response);
			
		}catch(CommandException e) {
			request.setAttribute("javax.servlet.jsp.jspException", e);
			nextPage = error;
			System.out.println("오류 : " + e.getMessage());
		}
			
		// forwarding
		RequestDispatcher reqDp = getServletContext().getRequestDispatcher(testDir + nextPage);
		reqDp.forward(request, response);
	}
}
~~~

## Command
~~~java
package mvc.board.command;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public interface Command {
	public String execute(HttpServletRequest request, HttpServletResponse response) throws CommandException;
}
~~~

## CommandException
~~~java
package mvc.board.command;
public class CommandException extends Exception {
	  public CommandException() {
	  		super();
	  	}
	  	
	  public CommandException(String error) {
	  		super(error);
	  	}
}
~~~

## CommandNull
~~~java
package mvc.board.command;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class CommandNull implements Command {
	private String next;

	public CommandNull(String _next) {
		next = _next;
	}

	public String execute(HttpServletRequest request, HttpServletResponse response) throws CommandException {
		return next;
	}
}
~~~

## CommandList
~~~java
package mvc.board.command;
import java.util.List;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.board.model.*;
public class CommandList implements Command {
	private String next;
	private int totalRecCount;		// 전체 레코드 수	
	private int pageTotalCount;		// 전체 페이지 수
	private int countPerPage = 3;	// 한페이지당 레코드 수
	private int pageNo;				// 페이지 번호
	
	public CommandList(String _next) {
		next = _next;
	}

	public String execute(HttpServletRequest request , HttpServletResponse response) throws CommandException {
		try {
			String pNum = request.getParameter("page");
			List <BoardRec> mList = getArticleList(pNum);
			
			request.setAttribute("mList", mList);
			
			int pCount = getTotalPage();
			
			request.setAttribute("pCount", pCount);
		   
		}catch(BoardException ex) {
			throw new CommandException("CommandList.java < 목록 > " + ex.toString()); 
		}
		return next;
	}
	
	// pNum을 받아준다
		public List <BoardRec> getArticleList(String pNum) throws BoardException {
			// 페이지 번호에 따른 시작 레코드 번호(startRow)와 보여줄 마지막 레코드 번호(endRow) 추출
		/*
		 		전체 레코드 수가 9
		 		1 페이지 : 1 ~ 3
		 		2 페이지 : 4 ~ 6
		 		3 페이지 : 7 ~ 9
		 */
			// 첫페이지는 1로 만들어준다.
			pageNo = 1;
			// pNum에 null값이 아닐때만 pNum을 형변환해준다.
			if(pNum != null) pageNo = Integer.parseInt(pNum);
			
			int endRow = pageNo * countPerPage;
			int startRow = endRow - (countPerPage - 1);
			
			// 현재 페이지에 보여울 메세지 목록을 얻어옴
			List <BoardRec> mList = BoardDao.getInstance().selectList(startRow, endRow);			
				return mList;
		}
			
		public int getTotalPage() throws BoardException {
			// 전체 레코드 수를 얻어옴
			totalRecCount = BoardDao.getInstance().getTotalCount();
			
			// 전체 페이지 수를 구함
	/*
				     레코드수	     페이지수
		 			9		3
					10		4
		 			11		4
		 			12		4
		 			13		5
	*/
			pageTotalCount = totalRecCount / countPerPage;  
			if(totalRecCount % countPerPage > 0) {
				pageTotalCount++;
			}
			return pageTotalCount;
		}
}
~~~

## CommandInput
~~~java
package mvc.board.command;
import java.text.DecimalFormat;
import java.util.List;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.board.model.*;
public class CommandInput implements Command {
	private String next;

	public CommandInput(String _next) {
		next = _next;
	}
	
	public String execute(HttpServletRequest request, HttpServletResponse response) throws CommandException {
		try {
			BoardRec rec = new BoardRec();
			BoardDao dao = BoardDao.getInstance();
			
			rec.setWriterName(request.getParameter("writerName"));	// 작성자
			rec.setTitle(request.getParameter("title"));			// 제목
			rec.setContent(request.getParameter("content"));		// 내용
			rec.setPassword(request.getParameter("password"));		// 비밀번호
			int groupId = dao.getGroupId();
			rec.setGroupId(groupId);								// 그룹번호
			
/*
			groupId = 1 이라면		00000000001999999
			groupId = 1234 이라면 	00000001234999999
*/
			// 순서번호(sequence_no) 지정
			DecimalFormat dformat = new DecimalFormat("0000000000");
			rec.setSequenceNo(dformat.format(groupId) + "999999");
			
			rec.setArticleId(dao.insert(rec));
			
			//-------------------------------------------------------------
		    List <BoardRec> mList = dao.selectList();	
		    request.setAttribute("param", mList);
		    
		}catch(BoardException ex) {
			throw new CommandException("CommandInput.java < 입력시 > " + ex.toString()); 
		}
		return next;
	}
}
~~~

## CommandView
~~~java
package mvc.board.command;
import java.util.List;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.board.model.*;
public class CommandView implements Command {
	private String next;

	public CommandView(String _next) {
		next = _next;
	}
	
	public String execute(HttpServletRequest request , HttpServletResponse response) throws CommandException {
		try {
			int article_id = Integer.parseInt(request.getParameter("article_id"));
			BoardDao dao = BoardDao.getInstance();
			dao.increaseReadCount(article_id);
			BoardRec rec = dao.selectById(article_id);

		    request.setAttribute("rec", rec);

		}catch(BoardException ex) {
			throw new CommandException("CommandList.java < 게시물 > " + ex.toString()); 
		}
		return next;
	}
}
~~~

## CommandDelete
~~~java
package mvc.board.command;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.board.model.*;
public class CommandDelete implements Command{
	private String next;

	public CommandDelete( String _next ){
		next = _next;
	}
	
	public String execute(HttpServletRequest request, HttpServletResponse response ) throws CommandException {
		try {	
			int articleId = Integer.parseInt(request.getParameter("article_id"));	// 게시글번호
			String password = request.getParameter("password");						// 비밀번호
			
			int resultCnt = BoardDao.getInstance().delete(articleId, password);
			
			request.setAttribute("result", resultCnt);
			
		}catch(BoardException ex) {
			throw new CommandException("CommandDelete.java < 삭제 > " + ex.toString()); 
		}
		return next;			
	}
}
~~~

## CommandModify
~~~java
package mvc.board.command;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.board.model.*;
public class CommandModify implements Command {
	private String next;

	public CommandModify(String _next) {
		next = _next;
	}
	
	public String execute(HttpServletRequest request , HttpServletResponse response) throws CommandException {
		try {
			BoardRec rec = new BoardRec();
	        int article_id = Integer.parseInt(request.getParameter("articleId")); // BoardModifyForm에서 parameter를 받아온다.
	        rec.setArticleId(article_id);
	        rec.setTitle(request.getParameter("title"));
	        rec.setPassword(request.getParameter("password"));
	        rec.setContent(request.getParameter("content"));
	        
	        BoardDao dao = BoardDao.getInstance();							// dao에 식들이 있으므로 객체생성
	        if(dao.update(rec) !=0) {										// update가 잘 되었을 때만 조건을 수행한다.
	        	request.setAttribute("rec", dao.selectById(article_id));	// article_id에 맞게 수정된 값(조건에서 이미 수정이된상태)을 rec에 넣어준다
	        }
	         
			int resultCnt = BoardDao.getInstance().update(rec);
			
			request.setAttribute("result", resultCnt);

		}catch(BoardException ex) {
			throw new CommandException("CommandList.java < 수정 > " + ex.toString()); 
		}
		return next;
	}
}
~~~

## CommandReply
~~~java
package mvc.board.command;
import java.text.DecimalFormat;
import java.util.Date;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.board.model.*;
public class CommandReply implements Command {
	private String next;

	public CommandReply(String _next) {
		next = _next;
	}
	
	public String execute(HttpServletRequest request , HttpServletResponse response) throws CommandException {
		try {
			int parentId = 0;
			BoardRec rec = new BoardRec();
			
			String pId = request.getParameter("parentId");
			if(pId != null) parentId = Integer.parseInt(pId);
			
			BoardDao dao = BoardDao.getInstance();
			// 부모게시글의 레코드를 얻어옴
			BoardRec parent = dao.selectById(parentId);
			
			// 부모게시글을 체크
			checkParent(parent, parentId);
			
			// 답변글에 순서번호 구하기
			String maxSeqNum = parent.getSequenceNo();
			String minSeqNum = getSearchMinSeqNum(parent);
			
			String lastChildSeq = dao.selectLastSequenceNumber(maxSeqNum, minSeqNum);
			
			String sequenceNumber = getSequenceNumber(parent,lastChildSeq);
			
			rec.setGroupId(parent.getGroupId());					// 부모의 그룹번호와 동일하게 지정
			rec.setSequenceNo(sequenceNumber);						// 위에서 구한 답변글의 순서번호 지정
			rec.setPostingDate((new Date()).toString());			// 등록일
			rec.setWriterName(request.getParameter("writerName"));	// 작성자
			rec.setTitle(request.getParameter("title"));			// 제목
			rec.setContent(request.getParameter("content"));		// 내용
			rec.setPassword(request.getParameter("password"));		// 비밀번호
			
			int articleId = dao.insert(rec);
			rec.setArticleId(articleId);							// 게시글번호
			
			request.setAttribute("rec", rec);

		}catch(BoardException ex) {
			throw new CommandException("CommandList.java < 답글 > " + ex.toString()); 
		}
		return next;
	}
	
	/*
	 * 부모글이 존재하는지 부모글이 마지막 3단계인지 확인하는 함수
	 */
	private void checkParent(BoardRec parent, int pId) throws BoardException {
		if(parent == null) throw new BoardException("부모글이 존재하지 않음 : " + pId);
		
		int parentLevel = parent.getLevel();
		if(parentLevel == 3) throw new BoardException("3단계 마지막 레벨 글에는 답변을 달 수 없습니다.");
	}
	
	private String getSearchMinSeqNum(BoardRec parent) {
		String parentSeqNum = parent.getSequenceNo();
		DecimalFormat dFormat = new DecimalFormat("0000000000000000");
		long parentSeqLongValue = Long.parseLong(parentSeqNum);
		long searchMinLongValue = 0;
		
		switch(parent.getLevel()) {
		case 0 : searchMinLongValue = parentSeqLongValue / 1000000L * 1000000L; break;
		case 1 : searchMinLongValue = parentSeqLongValue / 10000L * 10000L; break;
		case 2 : searchMinLongValue = parentSeqLongValue / 100L * 100L; break;
		}
		return dFormat.format(searchMinLongValue);
	}
	
	private String getSequenceNumber(BoardRec parent, String lastChildSeq) throws BoardException {
		long parentSeqLong	= Long.parseLong(parent.getSequenceNo());
		int  parentLevel	= parent.getLevel();
		
		long decUnit = 0;
		if		(parentLevel == 0) {decUnit = 10000L;}
		else if	(parentLevel == 1) {decUnit = 100L;}
		else if (parentLevel == 2) {decUnit = 1L;}
		
		String sequenceNumber = null;
		
		DecimalFormat dFormat = new DecimalFormat("0000000000000000");
		if(lastChildSeq == null) { // 답변글이 없다면
			sequenceNumber = dFormat.format(parentSeqLong-decUnit);
		}else { // 답변글이 있다면, 마지막 답변글인지 확인
			String orderOfLastChildSeq = null;
			
			if(parentLevel == 0) {
				orderOfLastChildSeq = lastChildSeq.substring(10,12);
				sequenceNumber = lastChildSeq.substring(0, 12) + "9999";
			}else if(parentLevel == 1) {
				orderOfLastChildSeq = lastChildSeq.substring(12,14);
				sequenceNumber = lastChildSeq.substring(0, 14) + "99";				
			}else if(parentLevel == 2) {
				orderOfLastChildSeq = lastChildSeq.substring(14,16);
				sequenceNumber = lastChildSeq;			
			}
			
			if(orderOfLastChildSeq.equals("00")) {
				throw new BoardException("마지막 자식 글이 이미 존재합니다.");
			}
			
			long seq = Long.parseLong(sequenceNumber) - decUnit;
			sequenceNumber = dFormat.format(seq);
			
			return sequenceNumber; 
		}
		return sequenceNumber;
	}
}
~~~