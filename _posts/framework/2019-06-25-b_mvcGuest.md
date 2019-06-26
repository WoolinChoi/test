---
layout: post
title: mvcGuest
category: framework
tags: [java, framework, mvc, mvcGuest]
comments: false
---

# [mvcGuest]()

## Guest
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% String projectName = "/Jsp"; %>    
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Guest</title>
</head>
<body>
	메인화면이라 . . . 그냥 상상하고 . . . 
	<a href="<%= projectName %>/guest?cmd=list-page"> 방명록 </a><br/><br/>
	<img src="imgs/image.gif"><br/>
</body>
</html>
~~~

## ListMessage
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="mvc.guest.model.*" %>    
<%@ page import="java.util.List" %>
<%
	// Control에서 param을 넘겨받아 mList 변수에 지정
	List <Message> mList = (List<Message>)request.getAttribute("param");  
%>    
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>ListMessage</title>
</head>
<body>
	<!-- 방명록 남기기 상대경로 사용 -->
	<a href="guest?cmd=input-page">방명록 남기기 </a><br/><br/>
	<% if(mList == null){ %>
		남겨진 메세지가 하나도~~없습니다. <br>
	<% }else{ %>
	<table border="1">
		<% for(Message msg : mList){ %>
		<tr>	
			<td> <%= msg.getId() %> </td> 
			<td> <%= msg.getGuestName() %></td> 
			<td> <a href="guest?cmd=delete-page&messageId=<%= msg.getId() %>"> [ 삭제하기 ] </a></td>			
		</tr>
		<tr>
			<td colspan='3'> 
			<textarea cols=35 rows=3 style="font-family: '돋움', '돋움체'; font-size: 10pt; font-style: normal; line-height: normal; color: #003399;background-color:#D4EBFF;border:1 solid #00009C;"><%= msg.getMessage() %>
			</textarea>
			</td>
		</tr>
		<% } // for-end %>
	</table>
	<% } // else-end %>
</body>
</html>
~~~

## InsertMessage
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>InsertMessage</title>
	<script type="text/javascript">
		function checkFields() {
			var frmObj = document.frm;
			
			frmObj.action = "guest?cmd=input-do";
			frmObj.submit();
		}
	</script>
</head>

<body>
	<form name="frm" method="post">
		이름 : <input type="text" name="guestName"/><br/><br/>
		암호 : <input type="password" name="password"/><br/><br/>
		메세지 : <textarea name="message" rows="3" cols="30"></textarea><br/><br/>
		<input type="button" value="메세지 남기기" onclick="Javascript:checkFields()">
	</form>
</body>
</html>
~~~

## SaveMessage
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>SaveMessage</title>
</head>
<body>
	<font size="3" color="#bb44cc">
		방명록에 메세지를 남겼습니다. 
	</font><br/><br/><br/>
	<a href="guest?cmd=list-page"> [ 목록보기 ] </a>
</body>
</html>
~~~

## DeleteMessage
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String messageId = request.getParameter("messageId");
%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>DeleteMessage</title>
</head>

<body>
	메세지를 삭제하려면 암호를 입력하세요. <br/><br/>
	<form action="guest?cmd=delete-do" method="post">
		<input type="hidden" name="messageId" value="<%=messageId%>"/>
		암호 : <input type="password" name="password"/>
		<input type="submit" value="메세지 삭제"/>
	</form>
</body>
</html>
~~~

## DeleteConfirm
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	Integer result = (Integer)request.getAttribute("result");
%>    
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>DeleteConfirm</title>
</head>

<body>
	<% if(result == 0){ %>
		삭제할 메세지가 존재하지 않거나 비밀번호가 올바르지 않습니다.
	<% }else{ %>
		메세지를 삭제하였습니다.
	<% } %>
	<br/><br/>
	<a href="guest?cmd=list-page"> [ 목록보기 ] </a>
</body>
</html>
~~~

## Error
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Error</title>
</head>

<body>
	<center>
	죄송합니다요. 네트워크 문제가 발생하였습니다. <br/><br/>
	<img src="mvcGuest/imgs/error.png"><br/>
	</center>
</body>
</html>
~~~

## Message
~~~java
package mvc.guest.model;
public class Message {
	private int id;
	private String guestName;
	private String password;
	private String message;
	
	public Message(){}
	
	public Message(int id, String guestName, String password, String message) {
		this.id			= id;
		this.guestName	= guestName;
		this.password	= password;
		this.message	= message;
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getGuestName() {
		return guestName;
	}
	public void setGuestName(String guestName) {
		this.guestName = guestName;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
}
~~~

## MessageException
~~~java
package mvc.guest.model;
public class MessageException extends Exception {
  public MessageException() {
  		super();
  	}
  	
  public MessageException(String error) {
  		super(error);
  	}	
}
~~~

## MessageDao
~~~java
package mvc.guest.model;
import java.sql.*;
import java.util.*;
public class MessageDao {
	// Single Pattern 
	private static MessageDao instance;
	
	// DB 연결시  관한 변수 
	private static final String 	dbDriver	=	"oracle.jdbc.driver.OracleDriver";
	private static final String		dbUrl		=	"jdbc:oracle:thin:@192.168.0.116:1521:orcl";
	private static final String		dbUser		=	"team5";
	private static final String		dbPass		=	"1004";
	
	private Connection	 		con;	
	
	//--------------------------------------------
	//#####	 객체 생성하는 메소드 
	public static MessageDao getInstance() throws MessageException {
		if(instance == null) {
			instance = new MessageDao();
		}
		return instance;
	}
	
	private MessageDao() throws MessageException {
		try {
			/********************************************
				1. 오라클 드라이버를 로딩
					( DBCP 연결하면 삭제할 부분 )
			*/
			Class.forName(dbDriver);	
		}catch(Exception ex) {
			throw new MessageException("방명록 ) DB 연결시 오류  : " + ex.toString());	
		}
		
	}
	
	/*
	 * 메세지를 입력하는 함수
	 */
	public int insert(Message rec) throws MessageException {
		PreparedStatement ps = null;
		
		try {
			con	= DriverManager.getConnection(dbUrl, dbUser, dbPass);
			String sql = "INSERT INTO guestTB VALUES(seq_messageId_guestTb.nextval, ?, ?, ?)";  

			ps = con.prepareStatement(sql);
			ps.setString(1, rec.getGuestName());
			ps.setString(2, rec.getPassword());
			ps.setString(3, rec.getMessage());
			
			return ps.executeUpdate();
					
		}catch(Exception ex) {
			throw new MessageException("방명록 ) DB에 입력시 오류  : " + ex.toString());	
		}finally {
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}
	}
	
	/*
	 * 메세지 목록 전체를 얻어올 때
	 */
	public List<Message> selectList() throws MessageException {
		PreparedStatement ps = null;
		ResultSet rs = null;
		List<Message> mList = new ArrayList<Message>();
		boolean isEmpty = true;
		
		try {
			con	= DriverManager.getConnection(dbUrl, dbUser, dbPass);
			String sql = "SELECT * FROM guestTB order by message_id desc";  
			ps = con.prepareStatement(sql);
			rs = ps.executeQuery();
			while(rs.next()) {
				isEmpty = false;
				
				int message_id = rs.getInt("message_id");
				String guest_name = rs.getString("guest_name");
				String password = rs.getString("password");
				String message = rs.getString("message");
				
				Message m = new Message(message_id, guest_name, password, message );
				mList.add(m);
			}
			
			if(isEmpty) return Collections.emptyList();
			
			return mList;
		}catch(Exception ex) {
			throw new MessageException("방명록 ) DB에 목록 검색시 오류  : " + ex.toString());	
		}finally {
			if(rs   != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}		
	}
	
	/* -------------------------------------------------------
	 * 현재 페이지에 보여울 메세지 목록  얻어올 때
	 */
	public List<Message> selectList(int firstRow, int endRow) throws MessageException {
		PreparedStatement ps = null;
		ResultSet rs = null;
		List<Message> mList = new ArrayList<Message>();
		boolean isEmpty = true;
		
		try {
			con	= DriverManager.getConnection(dbUrl, dbUser, dbPass);
			String sql = "SELECT * FROM guestTB	"
						+ "WHERE message_id IN "
						+ "	( SELECT message_id FROM ( SELECT message_id, rownum AS rnum "
						+ "	  FROM ( SELECT message_id FROM guestTB  ORDER BY message_id DESC ) ) "
						+ "	  WHERE rnum >= ? AND rnum <= ? ) "
						+ " ORDER BY message_id DESC";  
			ps = con.prepareStatement(sql);
			ps.setInt(1, firstRow);
			ps.setInt(2, endRow );
			rs = ps.executeQuery();
			
			while(rs.next()) {
				isEmpty = false;
				
				int message_id = rs.getInt("message_id");
				String guest_name = rs.getString("guest_name");
				String password = rs.getString("password");
				String message = rs.getString("message");
				
				Message m = new Message(message_id, guest_name, password, message);
				mList.add(m);
			}
			
			if(isEmpty) return Collections.emptyList();
			
			return mList;
		}catch(Exception ex) {
			throw new MessageException("방명록 ) DB에 목록 검색시 오류  : " + ex.toString());	
		}finally {
			if(rs   != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}		
	}	
	
	/* -------------------------------------------------------
	 * 메세지 전체 레코드 수를 검색
	 */
	public int getTotalCount() throws MessageException {
		PreparedStatement ps = null;
		ResultSet rs = null;
		
		try {
			con	= DriverManager.getConnection(dbUrl, dbUser, dbPass);
			String sql = "SELECT count(*) FROM guestTB";  
			ps = con.prepareStatement(sql);
			rs = ps.executeQuery();
			rs.next();		
			return  rs.getInt(1);
			
		}catch(Exception ex) {
			throw new MessageException("방명록 ) DB에 목록 검색시 오류  : " + ex.toString());	
		}finally {
			if(rs   != null) {try {rs.close();} catch(SQLException ex) {}}
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}			
	}
	
	/*
	 * 메세지 번호와 비밀번호에 의해 메세지 삭제
	 */
	public int delete(int messageId, String password) throws MessageException {
		PreparedStatement ps = null;
		
		try {
			con	= DriverManager.getConnection(dbUrl, dbUser, dbPass);
			
			String sql = "DELETE FROM guestTB WHERE message_id=? AND password=?";  
			ps = con.prepareStatement(sql);
			ps.setInt(1, messageId);
			ps.setString(2, password);
			
			return ps.executeUpdate();
		}catch(Exception ex) {
			throw new MessageException("방명록 ) DB에 삭제시 오류  : " + ex.toString());	
		}finally {
			if(ps   != null) {try {ps.close();} catch(SQLException ex) {}}
			if(con  != null) {try {con.close();} catch(SQLException ex) {}}
		}		
	}
}
~~~

## GuestControl
~~~java
package mvc.guest.control;
import java.io.IOException;
import java.util.HashMap;
import javax.servlet.*;
import javax.servlet.http.*;
import mvc.guest.command.*;
public class GuestControl extends HttpServlet {
	private HashMap commandMap;
	private String	jspDir = "/05_mvc_class/2_mvcGuest/";
	private String  error = "error.jsp";

    public GuestControl() {
        super();       
		initCommand();
	}

	private void initCommand() {
		commandMap = new HashMap();

		commandMap.put("main-page",	new CommandNull("main.jsp"));
		commandMap.put("list-page",	new CommandList("listMessage.jsp"));
		// 나머지도 추가하기
		commandMap.put("input-page", new CommandNull("insertMessage.jsp"));
		commandMap.put("input-do", new CommandInput("listMessage.jsp"));
		commandMap.put("delete-page", new CommandNull("deleteMessage.jsp"));
		commandMap.put("delete-do", new CommandDelete("deleteConfirm.jsp"));
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
		String cmdKey	= request.getParameter("cmd");
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
		RequestDispatcher reqDp = getServletContext().getRequestDispatcher(jspDir + nextPage);
		reqDp.forward(request, response);
	}
}
~~~

## Command
~~~java
package mvc.guest.command;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public interface Command {
	public String execute(HttpServletRequest request, HttpServletResponse response) throws CommandException;
}
~~~

## CommandException
~~~java
package mvc.guest.command;
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
package mvc.guest.command;
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
package mvc.guest.command;
import java.util.List;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.guest.model.*;
public class CommandList implements Command {
	private String next;

	public CommandList(String _next) {
		next = _next;
	}

	public String execute(HttpServletRequest request , HttpServletResponse response) throws CommandException {
		try {		
		    List <Message> mList = MessageDao.getInstance().selectList();	
		    request.setAttribute("param", mList);

		}catch(MessageException ex) {
			throw new CommandException("CommandList.java < 목록보기시 > " + ex.toString()); 
		}
		return next;
	}
}
~~~

## CommandInput
~~~java
package mvc.guest.command;
import java.util.List;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.guest.model.*;
public class CommandInput implements Command {
	private String next;

	public CommandInput(String _next) {
		next = _next;
	}
	
	public String execute(HttpServletRequest request, HttpServletResponse response) throws CommandException {
		try {
			Message msg = new Message();
			msg.setGuestName(request.getParameter("guestName"));
			msg.setPassword(request.getParameter("password"));
			msg.setMessage(request.getParameter("message"));
			
			MessageDao dao = MessageDao.getInstance();
			dao.insert(msg);
			
			//-------------------------------------------------------------
		    List <Message> mList = dao.selectList();	
		    request.setAttribute("param", mList );
		    
		}catch(MessageException ex) {
			throw new CommandException("CommandInput.java < 입력시 > " + ex.toString()); 
		}
		return next;
	}
}
~~~

## CommandDelete
~~~java
package mvc.guest.command;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import mvc.guest.model.*;
public class CommandDelete implements Command {
	private String next;

	public CommandDelete(String _next) {
		next = _next;
	}
	
	public String execute(HttpServletRequest request, HttpServletResponse response) throws CommandException {
		try {
			int messageId = Integer.parseInt(request.getParameter("messageId"));
			String password = request.getParameter("password");
			
			int resultCnt = MessageDao.getInstance().delete(messageId, password);
			
			request.setAttribute("result", resultCnt);
		}catch(MessageException ex) {
			throw new CommandException("CommandDelete.java < 삭제시 > " + ex.toString()); 
		}
		return next;			
	}
}
~~~